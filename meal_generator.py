from db_connector import connect_db, get_foods
import random

# 生成主餐
def generate_main_meal(conn, calorie_target, protein_target):
    """
    从数据库中随机组合出一组正餐，这组正餐将由主食，蛋白质，蔬菜组成,并尽量靠近设定的热量与蛋白质目标。
    返回包含类型、食材项、总热量和总蛋白质的词典，
    """
    cursor = conn.cursor(dictionary=True)

    # 获取所有的分类数据
    main = random.choice(get_foods("main"))
    protein = random.choice(get_foods("protein"))
    vegetable = random.choice(get_foods("vegetable"))

    meal = {
        "main": main,
        "protein": protein,
        "vegetable": vegetable
    }

    # 计算总热量和蛋白质
    total_cal = sum(item["calorie"] for item in meal.values())
    total_protein = sum(item["protein"] for item in meal.values())

    return{
        "type": "main_meal",
        "meal_items": meal,
        "total_calorie": round(total_cal, 1),
        "total_protein": round(total_protein, 1),
    }

# 生成加餐
def generate_snack(conn):
    """
    从数据库中随机组合出一次加餐，加餐由水果和乳制品组成。
    返回包含类型、食材项、总热量和总蛋白质的词典。
    """
    cursor = conn.cursor(dictionary=True)

    # 获取所有的分类数据
    fruit = random.choice(get_foods("fruit"))
    dairy = random.choice(get_foods("dairy"))

    snack = {
        "fruit": fruit,
        "dairy": dairy
    }

    total_cal = sum(item["calorie"] for item in snack.values())
    total_protein = sum(item["protein"] for item in snack.values())

    return {
        "type": "snack",
        "item": snack,
        "total_calorie": round(total_cal, 1),
        "total_protein": round(total_protein, 1)
    }

# 生成每日食谱（两餐+可选加餐）
def generate_daily_meal(conn, protein_range=(130, 150)):    #calorie_range在此后可能更改
    """
    生成一日菜单：
        - 两顿主餐（main + protein + vegetable）
        - 若总日热量低于目标的90%，自动添加加餐（fruit + dairy）
    """

    target_cal = 1700
    cal_lower_bound = target_cal - 100
    cal_upper_bound = target_cal + 100
    protein_lower, protein_upper = protein_range

    # 生成两顿主餐
    meal_lunch = generate_main_meal(conn, target_cal / 2, target_protein / 2)
    meal_dinner = generate_main_meal(conn, target_cal / 2, target_protein / 2)

    total_main_cal = meal_lunch["total_calorie"] + meal_dinner["total_calorie"]
    total_main_protein = meal_dinner["total_protein"] + meal_dinner["total_protein"]

    # 若主餐总热量小于下限，则重新生成晚餐直到满足条件
    while total_main_cal < lower_bound:
        meal_dinner = generate_main_meal(conn, target_cal / 2, target_protein / 2)
        total_main_cal = meal_lunch["total_calorie"] + meal_dinner["total_calorie"]
        total_main_protein = meal_lunch["total_protein"] + meal_dinner["total_protein"]

    # 若主餐低于下限，则自动添加snack
    snack_included = False
    snack = None

    if total_main_cal < lower_bound:
        snack = generate_snack(conn)
        total_main_cal += snack["total_calorie"]
        total_main_protein += snack["total_protein"]
        snack_included = True

        # 若超出上限则重新生成snack
        while total_main_cal > upper_bound:
            snack = generate_snack(conn)
            total_main_cal = (meal_lunch["total_calorie"] +
                              meal_dinner["total_calorie"] +
                              snack["total_calorie"])
            total_main_protein = (meal_lunch["total_protein"] +
                                  meal_dinner["total_protein"] +
                                  snack["total_protein"])

    # 整合返回结果
    meals = [meal_lunch, meal_dinner]
    if snack_included:
        meals.append(snack)

    return{
        "meals": meals,
        "total_calorie": round(total_main_cal, 1),
        "total_protein": round(total_main_protein, 1),
        "target": {"calorie": target_cal, "protein": target_protein},
        "snack_included": snack_included
    }

# 生成7日计划
def generate_weekly_meal_plan(conn):
    """
    自动生成7天的菜单。
    """
    weekly_plan = []
    for day in range(1,8):
        daily_plan = generate_daily_meal(conn)
        weekly_plan.append({"day": day, **daily_plan})
    return weekly_plan