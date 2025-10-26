from db_connector import connect_db, get_foods
import random

# 生成单个餐食的信息
def generate_single_meal(conn, calorie_target, protein_target):
    # 从数据库中随机组合出一顿正餐，这顿饭将由主食，蛋白质，蔬菜,并尽量靠近设定的热量与蛋白质目标。
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
        "meal_items": meal,
        "total_calorie": total_cal,
        "total_protein": total_protein
    }
