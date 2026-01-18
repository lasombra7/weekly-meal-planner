from user_service import generate_weekly_plan_for_user

for uid in[1, 2, 3]:
    result = generate_weekly_plan_for_user(user_id=uid)
    print(f"user_id={uid}")
    print("mode:", result["mode"])
    print("target:", result["targets"])
    print("week plan:\n", result["weekly_plan"])
    print("-" * 30)