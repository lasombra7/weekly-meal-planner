from user_service import generate_weekly_plan_for_user, load_latest_weekly_plan

plan = load_latest_weekly_plan(user_id=1)
print(plan["plan_date"])
print(plan["created_at"])
print(plan["weekly_plan"])
print(plan["weekly_plan"][0])