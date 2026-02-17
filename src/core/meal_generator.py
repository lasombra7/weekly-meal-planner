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
TWO_MEAL_DISTRIBUTION = {"lunch": 0.4,"dinner": 0.6}
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
    mains = get_foods("main")
    proteins = get_foods("protein")
    vegetables = get_foods("vegetable")

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
    fruit = random.choice(get_foods("fruit"))
    dairy = random.choice(get_foods("dairy"))

    snack = {
        "fruit": fruit,
        "dairy": dairy
    }

    total_cal = sum(item["calorie_per_100g"] for item in snack.values())
    total_protein = sum(item["protein_per_100g"] for item in snack.values())

    return {
        "type": "snack",
        "items": snack,
        "total_calorie": round(total_cal, 1),
        "total_protein": round(total_protein, 1)
    }

def scale_main_meal_portions(meal,target_cal, protein_range):
    """
    对单顿 maim 进行分量缩放：
    - vegetable 先固定为 200g，后续走离散档位搜索微调
    - protein / main 走离散档位搜索，满足calorie / protein 约束后选最优
    """

    protein_lower_bound, protein_upper_bound = protein_range
    calorie_lower_bound = target_cal * 0.8
    calorie_upper_bound = target_cal * 1.05
    protein_options = [50, 100, 150, 200, 250, 300]
    main_options = [50, 100, 150, 200, 250, 300, 350, 400]
    protein_tol_low = protein_lower_bound - 15
    protein_tol_high = protein_lower_bound + 5

    # 根据每100g营养素和实际克重计算总值
    def calc_totals(items):
        total_cal = 0.0
        total_protein = 0.0
        for v in items.values():
            grams = float(v.get("grams", 100))
            total_cal += float(v["calorie_per_100g"]) * grams / 100.0
            total_protein += float(v["protein_per_100g"]) * grams / 100.0
        return total_cal, total_protein

    # 第一步：固定蔬菜200g
    meal["meal_items"]["vegetable"]["grams"] = 200
    best_candidate = None
    best_score = None
    protein_weight = 4
    calorie_weight = 1

    # 第二步：先遍历protein，再遍历main
    for p_g in protein_options:
        meal["meal_items"]["protein"]["grams"] = p_g
        for m_g in main_options:
            meal["meal_items"]["main"]["grams"] = m_g
            total_cal, total_protein = calc_totals(meal["meal_items"])
            # 硬约束：不允许超过上限
            if total_cal > calorie_upper_bound:
                continue
            if total_protein > protein_upper_bound:
                continue

            # 主餐必须达到calorie_lower_bound
            if total_cal < calorie_lower_bound:
                continue
            # 优先接近protein_tol_low
            if not (protein_tol_low <= total_protein <= protein_tol_high):
                continue

            # 评分规则：优先接近protein_tol_low，再热量接近target
            protein_gap = abs(total_protein - protein_lower_bound)
            calorie_gap = abs(total_cal - target_cal)
            score = protein_weight * protein_gap + calorie_weight * calorie_gap
            if best_score is None or score < best_score:
                best_score = score
                best_candidate = {
                    "main_g": m_g,
                    "protein_g":p_g,
                    "vegetable_g": 200,
                    "total_cal": total_cal,
                    "total_protein": total_protein,
                }

    # 第三步：增加一个fallback。（若找不到完全满足的组合，做一次降级选择）
    if best_candidate is None:
        fallback_best = None
        fallback_score = None
        protein_weight = 4
        calorie_weight = 1

        for p_g in protein_options:
            meal["meal_items"]["protein"]["grams"] = p_g
            for m_g in main_options:
                meal["meal_items"]["main"]["grams"] = m_g
                total_cal, total_protein = calc_totals(meal["meal_items"])
                if total_cal > calorie_upper_bound:
                    continue
                if total_protein > protein_upper_bound:
                    continue
                #降级时允许calorie < lower_bound，但是仍优先靠近 protein_lower, 再靠近 target_cal
                protein_gap = abs(total_protein - protein_lower_bound)
                calorie_gap = abs(total_cal - target_cal)
                score = protein_weight * protein_gap + calorie_weight * calorie_gap
                if fallback_score is None or score < fallback_score:
                    fallback_score = score
                    fallback_best = {
                        "main_g": m_g,
                        "protein_g": p_g,
                        "vegetable_g": 200,
                        "total_cal": total_cal,
                        "total_protein": total_protein,
                    }

        best_candidate = fallback_best

    # 第四步： 把最优结果写回meal,并更新总宏：
    if best_candidate is not None:
        meal["meal_items"]["main"]["grams"] = best_candidate["main_g"]
        meal["meal_items"]["protein"]["grams"] = best_candidate["protein_g"]
        meal["meal_items"]["vegetable"]["grams"] = best_candidate["vegetable_g"]
        meal["total_calorie"] = round(best_candidate["total_cal"], 1)
        meal["total_protein"] = round(best_candidate["total_protein"], 1)
    return meal

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

    cal_lower_bound = target_cal - 100
    cal_upper_bound = target_cal + 100
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
    for day in range(1,8):
        daily_plan = generate_daily_meal_with_structure(conn, target_cal=target_cal, protein_range=protein_range, meal_structure=meal_structure)
        weekly_plan.append({"day": day, **daily_plan})
    return weekly_plan