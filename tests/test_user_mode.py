from src.core.user_service import load_latest_weekly_plan
from src.db.db_connector import connect_db

conn = connect_db()
try:
    plan = load_latest_weekly_plan(user_id=1, conn=conn)
    print(plan["plan_date"])
    print(plan["created_at"])
    print(plan["weekly_plan"])
    print(plan["weekly_plan"][0])

finally:
    conn.close()