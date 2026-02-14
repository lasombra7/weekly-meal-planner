from user_service import generate_weekly_plan_for_user

result = generate_weekly_plan_for_user(user_id=1)
print(result["weekly_metrics"])