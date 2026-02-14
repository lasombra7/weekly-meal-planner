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
    print("\n Today's Menu Recommendations：")
    for category, item in meal.items():
        print(f"{category.capitalize():<10} : {item['name']} ({item['calorie']}kcal, {item['protein']}g protein)")
    print(f"\nTotal calorie： {total_calorie} kcal")
    print(f"\nTotal protein: {total_protein} g")

    return meal

# 从 user_profile 表中加载用户信息
def load_user_profile(user_id):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM user_profile WHERE user_id = %s",
        (user_id,)
    )
    profile = cursor.fetchone()
    cursor.close()
    conn.close()

    if profile is None:
        raise ValueError(f"user_profile not found for user_id={user_id}")

    return profile


#模块测试入口
if __name__ == "__main__":
    get_random_meal()