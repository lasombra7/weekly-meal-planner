from src.db.db_connector import connect_db, get_foods
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

# 生成主餐
def generate_main_meal(conn, calorie_target, protein_target, strategy=None):
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
        "main": main,
        "protein": protein,
        "vegetable": vegetable
    }

    # 计算总热量和蛋白质
    total_cal = sum(item["calorie_per_100g"] for item in meal.values())
    total_protein = sum(item["protein_per_100g"] for item in meal.values())

    return{
        "type": "main_meal",
        "meal_items": meal,
        "total_calorie": round(total_cal, 1),
        "total_protein": round(total_protein, 1),
    }

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

# 生成两餐制每日食谱（两餐+可选加餐）
def generate_two_meal_day(conn,
                        target_cal = 1700,
                        protein_range=(130, 150)):    #calorie_range在此后可能更改
    """
    生成一日菜单(two_meal_day)：
        - Lunch + Dinner 主餐中包括 main + protein + vegetable
        - 若总日热量低于target_cal，自动添加snack（fruit + dairy）
    """

    cal_lower_bound = target_cal - 100
    cal_upper_bound = target_cal + 100
    protein_lower_bound, protein_upper_bound = protein_range

    lunch_ratio = TWO_MEAL_DISTRIBUTION["lunch"]
    dinner_ratio = TWO_MEAL_DISTRIBUTION["dinner"]

    # 生成两顿主餐(Lunch + Dinner)
    for _ in range(50):
        meal_lunch = generate_main_meal(conn, target_cal * lunch_ratio, protein_lower_bound * lunch_ratio)
        meal_dinner = generate_main_meal(conn, target_cal * dinner_ratio, protein_lower_bound * dinner_ratio)

        total_main_cal = meal_lunch["total_calorie"] + meal_dinner["total_calorie"]
        total_main_protein = meal_lunch["total_protein"] + meal_dinner["total_protein"]

        if (cal_lower_bound <= total_main_cal <= cal_upper_bound
            and protein_lower_bound <= total_main_protein <= protein_upper_bound):
            break

    # 生成snack
    snack = generate_snack(conn)
    snack_allowed = False

    #若主餐热量不足目标值（现1700），则生成snack
    if total_main_cal < target_cal:
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
    for _ in range(50):
        meal_breakfast = generate_main_meal(conn, target_cal * breakfast_ratio, protein_lower_bound * breakfast_ratio)
        meal_lunch = generate_main_meal(conn, target_cal * lunch_ratio, protein_lower_bound * lunch_ratio)
        meal_dinner = generate_main_meal(conn, target_cal * dinner_ratio, protein_lower_bound * dinner_ratio)

        total_main_cal = meal_breakfast["total_calorie"] + meal_lunch["total_calorie"] + meal_dinner["total_calorie"]
        total_main_protein = meal_breakfast["total_protein"] + meal_lunch["total_protein"] + meal_dinner["total_protein"]

        if (cal_lower_bound <= total_main_cal <= cal_upper_bound
            and protein_lower_bound <= total_main_protein <= protein_upper_bound):
            break

    # 生成snack
    snack = generate_snack(conn)
    snack_allowed = False

    # 若主餐热量不足目标值（现1700），则生成snack
    if total_main_cal < target_cal:
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

#方便测试时候整洁，后期可删除
if __name__ == "__main__":
    conn = connect_db()
    # ===== 原 Weekly 逻辑 =====
    print("=== Weekly Plan (Default: Random Strategy) ===")
    weekly_plan = generate_weekly_meal_plan(conn, meal_structure="three_meals")
    for day in weekly_plan:
        print(f"Day {day['day']} - {day['total_calorie']} kcal / {day['total_protein']} g protein |")
        print(f"Snack allowed: {day['snack_allowed']}")
        print("-" * 60)

        # 打印每顿主餐详情
        for meal in day["meals"]:
            print(f"{meal['type'].title()}:")
            for category, item in meal["meal_items"].items():
                print(f"  -  {category.title()}:{item['name']} ({item['calorie_per_100g']} kcal, {item['protein_per_100g']} g protein)")
            print(f"  →  Total:{meal['total_calorie']} kcal, {meal['total_protein']} g protein \n")

        # 如果有snack，打印snack详情
        snack = day["snack_option"]
        print(f"Snack option({'Allowed' if day['snack_allowed'] else 'Optional only'}):")
        for category, item in snack["items"].items():
            print(f"  -  {category.title()}: {item['name']} ({item['calorie_per_100g']} kcal, {item['protein_per_100g']} g protein)")
        print(f"  →  Total:{snack['total_calorie']} kcal, {snack['total_protein']} g protein")
        print("=" * 60)

    # ===== 现测试Greedy Strategy =====
    print("\n=== Greedy Strategy Test ===")
    meal = generate_main_meal(
        conn,
        calorie_target=850,
        protein_target=70,
        strategy=get_strategy("greedy")
    )

    for category, item in meal["meal_items"].items():
        print(f"  -  {category.title()}: {item['name']} ({item['calorie_per_100g']} kcal, {item['protein_per_100g']} g protein)")
    print(f"  →  Total:{meal['total_calorie']} kcal, {meal['total_protein']} g protein \n")

    # ===== 现测试Weighted Strategy =====
    print("=== Weighted Strategy Test ===")
    meal = generate_main_meal(
        conn,
        calorie_target=850,
        protein_target=70,
        strategy=get_strategy("weighted")
    )

    for category, item in meal["meal_items"].items():
        print(f"  -  {category.title()}: {item['name']} ({item['calorie_per_100g']} kcal, {item['protein_per_100g']} g protein)")
    print(f"  →  Total:{meal['total_calorie']} kcal, {meal['total_protein']} g protein \n")

    conn.close()