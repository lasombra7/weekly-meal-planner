import mysql.connector

# 连接mysql数据库
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sha_0715",
    database="meal_planner"
)

cursor = conn.cursor(dictionary=True)

#读几条数据作为测试
cursor.execute("select * from protein;")
rows = cursor.fetchall()

print("Database connected successfully!\n")
for row in rows:
    print(row)

#清理资源
cursor.close()
conn.close()