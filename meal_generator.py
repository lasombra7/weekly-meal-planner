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
        "items": snack,
        "total_calorie": round(total_cal, 1),
        "total_protein": round(total_protein, 1)
    }

# 生成每日食谱（两餐+可选加餐）
def generate_daily_meal(conn, protein_range=(130, 150)):    #calorie_range在此后可能更改
    """
    生成一日菜单：
        - 两顿主餐（main + protein + vegetable）
        - 若总日热量低于target_cal，自动添加加餐（fruit + dairy）
    """

    target_cal = 1700
    cal_lower_bound = target_cal - 100
    cal_upper_bound = target_cal + 100
    protein_lower_bound, protein_upper_bound = protein_range

    # 生成两顿主餐
    for _ in range(50):
        meal_lunch = generate_main_meal(conn, target_cal / 2, protein_lower_bound / 2)
        meal_dinner = generate_main_meal(conn, target_cal / 2, protein_lower_bound / 2)

        total_main_cal = meal_lunch["total_calorie"] + meal_dinner["total_calorie"]
        total_main_protein = meal_lunch["total_protein"] + meal_dinner["total_protein"]

        if (cal_lower_bound <= total_main_cal <= cal_upper_bound
            and protein_lower_bound <= total_main_protein >= protein_upper_bound):
            break

    # 生成snack
    snack = generate_snack(conn)
    snack_allowed = False

    #若主餐热量不足1700，则生成snack
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

#方便测试时候整洁，后期可删除
if __name__ == "__main__":
    conn = connect_db()
    weekly_plan = generate_weekly_meal_plan(conn)
    for day in weekly_plan:
        print(f"Day{day['day']} - {day['total_calorie']} kcal / {day['total_protein']} g protein |")
        print(f"Snack allowed: {day['snack_allowed']}")
        print("-" * 60)

        # 打印每顿主餐详情
        for meal in day["meals"]:
            print(f"{meal['type'].title()}:")
            for category, item in meal["meal_items"].items():
                print(f"  -  {category.title()}:{item['name']}({item['calorie']} kcal, {item['protein']} g protein)")
                print(f"  →  Total:{meal['total_calorie']} kcal, {meal['total_protein']} g protein \n")

        # 如果有snack，打印snack详情
        snack = day["snack_option"]
        print(f"Snack option({'Allowed' if day['snack_allowed'] else 'Optional only'}):")
        for category, item in snack["items"].items():
            print(f"  -  {category.title()}: {item['name']} ({item['calorie']} kcal, {item['protein']} g protein)")
        print(f"  →  Total:{snack['total_calorie']} kcal, {snack['total_protein']} g protein")
        print("=" * 60)

conn.close()