from src.db.db_connector import get_foods
from src.strategies.registry import get_strategy
import random


def generate_daily_meal_with_structure(conn, target_cal, protein_range, meal_structure="two_meals", strategy=None):
    """
    区分生成 two_meal_day 还是 three_meal_day。
    two_meal_day: Lunch 分配 40% calorie, 40% protein。 Dinner 分配 60% calorie, 60% protein。
    three_meal_day: Breakfast 分配 25% calorie, 25% protein。 Lunch 分配 35% calorie, 35% protein。 Dinner 分配 40% calorie, 40% protein。
    """

    if meal_structure == "two_meals":
        return generate_two_meal_day(conn, target_cal,protein_range)
    elif meal_structure == "three_meals":
        return generate_three_meal_day(conn, target_cal, protein_range)
    else:
        raise ValueError("Unknown meal_structure")

# 两餐制分配比例
TWO_MEAL_DISTRIBUTION = {"lunch": 0.45,"dinner": 0.55}
assert abs(
    TWO_MEAL_DISTRIBUTION["lunch"] + TWO_MEAL_DISTRIBUTION["dinner"] - 1.0
) < 1e-6, "TWO_MEAL_DISTRIBUTION ratios must sum to 1.0"

# 三餐制分配比例
THREE_MEAL_DISTRIBUTION = {"breakfast": 0.25, "lunch": 0.35, "dinner": 0.4}
assert abs(
    THREE_MEAL_DISTRIBUTION["breakfast"] + THREE_MEAL_DISTRIBUTION["lunch"] + THREE_MEAL_DISTRIBUTION["dinner"] - 1.0
) < 1e-6, "THREE_MEAL_DISTRIBUTION ratios must sum to 1.0"

# 生成main
def generate_main_meal(conn, calorie_target, protein_range, strategy=None):
    """
    从数据库中随机组合出一组正餐，这组正餐将由main, protein, vegetable组成,并尽量靠近设定的热量与蛋白质目标。
    返回包含type, meal_item, total_calorie, total_protein的词典
    """
    if strategy is None:
        strategy = get_strategy("random")

    # 获取所有的分类数据
    mains = get_foods("main", conn)
    proteins = get_foods("protein", conn)
    vegetables = get_foods("vegetable", conn)

    # 由策略决定如何选择食材
    main = strategy.pick_main(mains)
    protein = strategy.pick_protein(proteins)
    vegetable = strategy.pick_vegetable(vegetables)

    meal = {
        "main": {**main,"grams": 100},
        "protein": {**protein,"grams": 100},
        "vegetable": {**vegetable,"grams": 100}
    }

    # 计算总热量和蛋白质
    total_cal = sum(item["calorie_per_100g"] * item["grams"] / 100 for item in meal.values())
    total_protein = sum(item["protein_per_100g"] * item["grams"] / 100 for item in meal.values())

    result = {
        "type": "main_meal",
        "meal_items": meal,
        "total_calorie": round(total_cal, 1),
        "total_protein": round(total_protein, 1),
    }

    result = scale_main_meal_portions(result, calorie_target, protein_range)
    return result

# 生成加餐
def generate_snack(conn):
    """
    从数据库中随机组合出一次snack，snack由fruit和dairy组成。
    返回包含type, items, total_calorie, total_protein的词典。
    """
    cursor = conn.cursor(dictionary=True)

    # 获取所有的分类数据
    fruit = random.choice(get_foods("fruit", conn))
    dairy = random.choice(get_foods("dairy", conn))

    snack = {
        "fruit": fruit,
        "dairy": dairy
    }

    total_cal = sum(item["calorie_per_100g"] for item in snack.values())
    total_protein = sum(item["protein_per_100g"] for item in snack.values())

    return {
        "type": "snack",
        "snack_items": snack,
        "total_calorie": round(total_cal, 1),
        "total_protein": round(total_protein, 1)
    }

def scale_main_meal_portions(meal,target_cal, protein_range):
    """
    对单顿 maim 进行分量缩放：
    - vegetable 先固定为 200g
    - protein / main 走离散档位搜索，
    - 优先满足硬约束，若失败则fallback
    - 增加 decision_trace 用于解释 protein 决策
    """

    protein_lower_bound, protein_upper_bound = protein_range
    calorie_lower_bound = target_cal * 0.8
    calorie_upper_bound = target_cal * 1.05
    protein_target = (protein_lower_bound + protein_upper_bound) / 2
    protein_options = [50, 100, 150, 200, 250, 300]
    main_options = [50, 100, 150, 200, 250, 300, 350, 400]

    # 固定蔬菜200g
    meal["meal_items"]["vegetable"]["grams"] = 200

    # 根据每100g营养素和实际克重计算总值
    def calc_totals(items):
        total_cal = 0.0
        total_protein = 0.0
        for v in items.values():
            grams = float(v.get("grams", 100))
            total_cal += float(v["calorie_per_100g"]) * grams / 100.0
            total_protein += float(v["protein_per_100g"]) * grams / 100.0
        return total_cal, total_protein

    def search(strict_mode=True):
        best_candidate = None
        best_score = None
        # 权重：蛋白优先
        protein_weight = 4 if strict_mode else 3
        calorie_weight = 1

        # 先遍历protein，再遍历main
        for p_g in protein_options:
            meal["meal_items"]["protein"]["grams"] = p_g
            for m_g in main_options:
                meal["meal_items"]["main"]["grams"] = m_g
                total_cal, total_protein = calc_totals(meal["meal_items"])
                # 硬约束：不允许超过 calorie & protein upper bound
                if total_cal > calorie_upper_bound:
                    continue
                if total_protein > protein_upper_bound:
                    continue
                if strict_mode:
                    if total_cal < calorie_lower_bound:
                        continue

                # 评分规则：优先接近protein_tol_low，再热量接近target
                protein_gap = abs(total_protein - protein_target)
                calorie_gap = abs(total_cal - target_cal)
                score = protein_weight * protein_gap + calorie_weight * calorie_gap
                if best_score is None or score < best_score:
                    best_score = score
                    best_candidate = {
                        # 用于输出菜单
                        "main_g": m_g,
                        "protein_g":p_g,
                        "vegetable_g": 200,
                        "total_cal": total_cal,
                        "total_protein": total_protein,

                        # 用于生成解释
                        "protein_gap": protein_gap,
                        "calorie_gap": calorie_gap,
                        "strict_mode": strict_mode,
                        "protein_weight": protein_weight,
                        "calorie_weight": calorie_weight,
                    }
        return best_candidate

    # 先严格搜索
    best_candidate = search(strict_mode=True)
    # 若失败，fallback。（若找不到完全满足的组合，做一次降级选择）
    if best_candidate is None:
        best_candidate = search(strict_mode=False)

    # 把最优结果写回meal,并更新总宏
    if best_candidate is not None:
        # 用于输出菜单
        meal["meal_items"]["main"]["grams"] = best_candidate["main_g"]
        meal["meal_items"]["protein"]["grams"] = best_candidate["protein_g"]
        meal["meal_items"]["vegetable"]["grams"] = best_candidate["vegetable_g"]
        meal["total_calorie"] = round(best_candidate["total_cal"], 1)
        meal["total_protein"] = round(best_candidate["total_protein"], 1)

        # 用于生成解释
        meal["decision_trace"] = {
            "strict_mode_used": best_candidate["strict_mode"],
            "protein_weight": best_candidate["protein_weight"],
            "calorie_weight": best_candidate["calorie_weight"],
            "final_protein_gap": round(best_candidate["protein_gap"], 2),
            "final_calorie_gap": round(best_candidate["calorie_gap"], 2),
        }
    return meal

def scale_snack_portions(snack, total_main_cal, total_main_protein, target_cal, protein_range):
    """
    对snack 进行分量优化：
    - 补足 calorie / protein deficit
    - 不允许超过 calorie_upper_bound / protein_upper_bound
    - 如果 calorie 偏低则 fruit 优先走离散档位搜索，小分量 dairy 作为补充
    - 如果 protein 偏低则 dairy 优先走离散档位搜搜，小分量 fruit 作为补充
    """

    protein_lower_bound, protein_upper_bound = protein_range
    protein_target = (protein_lower_bound + protein_upper_bound) / 2
    calorie_upper_bound = target_cal * 1.05
    fruit_options = [50, 100, 150, 200]
    dairy_options = [50, 100, 150, 200]
    protein_deficit = protein_target - total_main_protein

    # 根据每100g营养素和实际克重计算总值
    def calc_snack_totals(items):
        total_cal = 0.0
        total_protein = 0.0
        for v in items.values():
            grams = float(v.get("grams", 100))
            total_cal += float(v["calorie_per_100g"]) * grams / 100.0
            total_protein += float(v["protein_per_100g"]) * grams / 100.0
        return total_cal, total_protein

    best_candidate = None
    best_score = None
    fallback_candidate = None
    fallback_score = None
    # 权重：蛋白优先
    protein_weight = 3
    calorie_weight = 1

    # 先遍历 fruit ，再遍历 dairy
    for f_g in fruit_options:
        snack["snack_items"]["fruit"]["grams"] = f_g
        for d_g in dairy_options:
            snack["snack_items"]["dairy"]["grams"] = d_g
            snack_cal, snack_protein = calc_snack_totals(snack["snack_items"])
            snack_allowed_total_cal = total_main_cal + snack_cal
            snack_allowed_total_protein = total_main_protein + snack_protein
            # 硬约束：不允许超过 calorie & protein upper bound
            if snack_allowed_total_cal > calorie_upper_bound:
                continue
            if snack_allowed_total_protein > protein_upper_bound:
                continue

            # 评分
            protein_gap = abs(snack_allowed_total_protein - protein_target)
            calorie_gap = abs(snack_allowed_total_cal - target_cal)
            # 偏向补偿逻辑
            if protein_deficit > 0:
                # protein 不足的时候优先靠近 protein
                score = protein_weight * protein_gap + calorie_weight * calorie_gap
            else:
                # protein 足够的时候优先补充 calorie
                score = calorie_weight * calorie_gap + 0.5 * protein_gap
            if best_score is None or score < best_score:
                best_score = score
                best_candidate = {
                    "fruit_g": f_g,
                    "dairy_g": d_g,
                    "total_cal": snack_allowed_total_cal,
                    "total_protein": snack_allowed_total_protein,
                }
            # 增加一个fallback。（若找不到完全满足的组合，做一次降级选择）
            fallback_score_temp = protein_gap + calorie_gap
            if fallback_score is None or fallback_score_temp < fallback_score:
                fallback_score = fallback_score_temp
                fallback_candidate = {
                "fruit_g": f_g,
                "dairy_g": d_g,
                "total_cal": snack_allowed_total_cal,
                "total_protein": snack_allowed_total_protein,
                }

    # 把最优结果写回meal,并更新总宏
    if best_candidate is None:
        best_candidate = fallback_candidate
    if best_candidate is not None:
        snack["snack_items"]["fruit"]["grams"] = best_candidate["fruit_g"]
        snack["snack_items"]["dairy"]["grams"] = best_candidate["dairy_g"]
        snack["total_calorie"] = round(best_candidate["total_cal"] - total_main_cal, 1)
        snack["total_protein"] = round(best_candidate["total_protein"] - total_main_protein, 1)
    return snack

# 生成两餐制每日食谱（两餐+可选加餐）
def generate_two_meal_day(conn,
                        target_cal = 1700,
                        protein_range=(130, 150)):    #calorie_range在此后可能更改
    """
    生成一日菜单(two_meal_day)：
        - Lunch + Dinner 主餐中包括 main + protein + vegetable
        - 若总日热量低于target_cal，自动添加snack（fruit + dairy）
    """

    cal_lower_bound = target_cal * 0.8
    cal_upper_bound = target_cal * 1.05
    protein_lower_bound, protein_upper_bound = protein_range

    lunch_ratio = TWO_MEAL_DISTRIBUTION["lunch"]
    dinner_ratio = TWO_MEAL_DISTRIBUTION["dinner"]

    # 生成两顿主餐(Lunch + Dinner)
    for _ in range(10):
        meal_lunch = generate_main_meal(
            conn,
            target_cal * lunch_ratio,
            (protein_lower_bound * lunch_ratio, protein_upper_bound * lunch_ratio)
        )
        meal_dinner = generate_main_meal(
            conn,
            target_cal * dinner_ratio,
            (protein_lower_bound * dinner_ratio, protein_upper_bound * dinner_ratio)
        )

        total_main_cal = meal_lunch["total_calorie"] + meal_dinner["total_calorie"]
        total_main_protein = meal_lunch["total_protein"] + meal_dinner["total_protein"]

        if (cal_lower_bound <= total_main_cal <= cal_upper_bound
            and protein_lower_bound <= total_main_protein <= protein_upper_bound):
            break

    # 生成snack
    snack = generate_snack(conn)
    snack = scale_snack_portions(snack, total_main_cal, total_main_protein, target_cal, protein_range)
    snack_allowed = False

    #若主餐热量不足目标值（现1700），则生成snack
    if total_main_cal < target_cal * 0.9:
        if ((total_main_cal + snack["total_calorie"]) <= cal_upper_bound
            and (total_main_protein + snack["total_protein"]) <= protein_upper_bound):
            snack_allowed = True

    # 计算总热量和蛋白质
    if snack_allowed:
        total_cal = total_main_cal + snack["total_calorie"]
        total_protein = total_main_protein + snack["total_protein"]
    else:
        total_cal = total_main_cal
        total_protein = total_main_protein

    #方便测试时候整洁，后期可删除
    total_cal = round(total_cal, 1)
    total_protein = round(total_protein, 1)

    # 整合返回结果
    meals = [meal_lunch, meal_dinner]
    return{
        "meals": meals,
        "snack_option": snack,
        "snack_allowed": snack_allowed,
        "total_calorie": round(total_cal, 1),
        "total_protein": round(total_protein, 1),
        "target": {
            "calorie": target_cal,
            "protein_lower_bound": protein_lower_bound,
            "protein_upper_bound": protein_upper_bound
        }
    }

# three_meal_day
def generate_three_meal_day(conn,target_cal, protein_range):
    """
    生成一日菜单(three_meal_day)：
        - Breakfast + Lunch + Dinner 主餐中包括 main + protein + vegetable
        - 若总日热量低于target_cal，自动添加snack（fruit + dairy）
    """

    cal_lower_bound = target_cal * 0.8
    cal_upper_bound = target_cal * 1.05
    protein_lower_bound, protein_upper_bound = protein_range

    breakfast_ratio = THREE_MEAL_DISTRIBUTION["breakfast"]
    lunch_ratio = THREE_MEAL_DISTRIBUTION["lunch"]
    dinner_ratio = THREE_MEAL_DISTRIBUTION["dinner"]

    # 生成三顿主餐(Breakfast + Lunch + Dinner)
    for _ in range(10):
        meal_breakfast = generate_main_meal(
            conn,
            target_cal * breakfast_ratio,
            (protein_lower_bound * breakfast_ratio, protein_upper_bound * breakfast_ratio)
        )
        meal_lunch = generate_main_meal(
        conn,
        target_cal * lunch_ratio,
        (protein_lower_bound * lunch_ratio, protein_upper_bound * lunch_ratio)
        )
        meal_dinner = generate_main_meal(
            conn,
            target_cal * dinner_ratio,
            (protein_lower_bound * dinner_ratio, protein_upper_bound * dinner_ratio)
        )

        total_main_cal = meal_breakfast["total_calorie"] + meal_lunch["total_calorie"] + meal_dinner["total_calorie"]
        total_main_protein = meal_breakfast["total_protein"] + meal_lunch["total_protein"] + meal_dinner["total_protein"]

        if (cal_lower_bound <= total_main_cal <= cal_upper_bound
            and protein_lower_bound <= total_main_protein <= protein_upper_bound):
            break

    # 生成snack
    snack = generate_snack(conn)
    snack = scale_snack_portions(snack, total_main_cal, total_main_protein, target_cal, protein_range)
    snack_allowed = False

    # 若主餐热量不足目标值（现1700），则生成snack
    if total_main_cal < target_cal * 0.9:
        if ((total_main_cal + snack["total_calorie"]) <= cal_upper_bound
                and (total_main_protein + snack["total_protein"]) <= protein_upper_bound):
            snack_allowed = True

    # 计算总热量和蛋白质
    if snack_allowed:
        total_cal = total_main_cal + snack["total_calorie"]
        total_protein = total_main_protein + snack["total_protein"]
    else:
        total_cal = total_main_cal
        total_protein = total_main_protein

    # 方便测试时候整洁，后期可删除
    total_cal = round(total_cal, 1)
    total_protein = round(total_protein, 1)

    # 整合返回结果
    meals = [meal_breakfast, meal_lunch, meal_dinner]
    return {
        "meals": meals,
        "snack_option": snack,
        "snack_allowed": snack_allowed,
        "total_calorie": round(total_cal, 1),
        "total_protein": round(total_protein, 1),
        "target": {
            "calorie": target_cal,
            "protein_lower_bound": protein_lower_bound,
            "protein_upper_bound": protein_upper_bound
        }
    }
# 生成7日计划
def generate_weekly_meal_plan(conn, target_cal=1700, protein_range=(130,150), meal_structure="two_meals"):
    """
    自动生成7天的菜单。
    """
    weekly_plan = []
    for day in range(1, 8):
        daily_plan = generate_daily_meal_with_structure(conn, target_cal=target_cal, protein_range=protein_range, meal_structure=meal_structure)
        weekly_plan.append({"day": day, **daily_plan})
    return weekly_plan