import mysql.connector
import random

# 连接mysql数据库
def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sha_0715",
        database="meal_planner",
        charset="utf8mb4"
    )
    return conn

#获取任意表的所有食材
def get_foods(table_name):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"select * from {table_name}")
    result =  cursor.fetchall()
    cursor.close()
    conn.close()
    return result

#随机选择出一顿饭（用于测试）
def get_random_meal():
    meal = {
        "main": random.choice(get_foods("main")),
        "protein": random.choice(get_foods("protein")),
        "vegetable":random.choice(get_foods("vegetable")),
        "fruit": random.choice(get_foods("fruit")),
        "oil":random.choice(get_foods("oil")),
        "dairy":random.choice(get_foods("dairy"))
    }

    #计算总热量和蛋白质
    total_calorie = sum(item["calorie"] for item in meal.values())
    total_protein = sum(item["protein"] for item in meal.values())

    #输出推荐部分
    print("\n 今日菜单推荐：")
    for category, item in meal.items():
        print(f"{category.capitalize():<10} : {item['name']} ({item['calorie']}kcal, {item['protein']}g 蛋白质)")
    print(f"\n总热量为： {total_calorie} kcal")
    print(f"\n总蛋白质为: {total_protein} g")

    return meal

#模块测试入口
if __name__ == "__main__":
    get_random_meal()