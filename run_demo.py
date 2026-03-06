from src.core.user_service import generate_weekly_plan_for_user

def print_meal_items(meal_items):
    # 打印单顿主餐里的食物信息
    # Print the food information in a single main meal
    for category, item in meal_items.items():
        name = item["name"]
        grams = item.get("grams", 100)
        calorie = item["calorie_per_100g"]
        protein = item["protein_per_100g"]
        print(f"    - {category.capitalize()}: {name} ({grams}g, {calorie} kcal/100g, {protein} g protein/100g)")

def print_snack(snack):
    # 打印加餐信息
    # Print snack information
    for category, item in snack["snack_items"].items():
        name = item["name"]
        grams = item.get("grams",100)
        calorie = item["calorie_per_100g"]
        protein = item["protein_per_100g"]
        print(f"    - {category.capitalize()}: {name} ({grams}g, {calorie} kcal/100g, {protein} g protein/100g)")

def main():
    # 运行访客模式 demo，生成一周meal plan
    # Run the guest mode demo and generate a one-week meal plan
    visitor_profile = {
        "height_cm": 180,
        "weight_kg": 75,
        "age": 28,
        "sex": "male",
        "activity_level": "moderate",
        "goal": "maintain",
        "meal_structure": "two_meals"
    }

    result = generate_weekly_plan_for_user(
        visitor_profile=visitor_profile,
        strategy_name="random"
    )

    print("=" * 60)
    print("Weekly Meal Planner Demo (Visitor Mode)")
    print("=" * 60)

    print("\nUser Profile")
    print(f"  Height: {result['user_profile']['height_cm']} cm")
    print(f"  Weight: {result['user_profile']['weight_kg']} kg")
    print(f"  Age: {result['user_profile']['age']}")
    print(f"  Sex: {result['user_profile']['sex']}")
    print(f"  Activity Level: {result['user_profile']['activity_level']}")
    print(f"  Goal: {result['user_profile']['goal']}")
    print(f"  Meal Structure: {result['user_profile']['meal_structure']}")

    print("\nTargets")
    print(f"  Calorie Target: {result['targets']['calorie']} kcal")
    print(f"  Protein Range: {result['targets']['protein_range'][0]} - {result['targets']['protein_range'][1]} g")
    print(f"  Strategy: {result['strategy_name']}")

    print("\n" + "=" * 60)
    print("Weekly Meal Plan")
    print("=" * 60)

    for day_index, day in enumerate(result["weekly_plan"], start=1):
        print(f"\nDay {day_index}")
        print("-" * 40)

        for meal_index, meal in enumerate(day["meals"], start=1):
            print(f"  Main Meal {meal_index}")
            print_meal_items(meal["meal_items"])
            print(f"    Total: {meal['total_calorie']} kcal, {meal['total_protein']} g protein")

        print(f"  Snack Allowed: {day['snack_allowed']}")
        if day["snack_allowed"]:
            print("  Snack")
            print_snack(day["snack_option"])
            print(f"    Total: {day['snack_option']['total_calorie']} kcal, {day['snack_option']['total_protein']} g protein")

        print(f"  Daily Total: {day['total_calorie']} kcal, {day['total_protein']} g protein")

    print("\n" + "=" * 60)
    print("Weekly Metrics")
    print("=" * 60)
    weekly_metrics = result["weekly_metrics"]
    print(f"Average Calorie Deviation: {weekly_metrics['avg_calorie_deviation']}")
    print(f"Average Protein Deviation: {weekly_metrics['avg_protein_deviation']}")
    print(f"Calorie Failure Days: {weekly_metrics['calorie_failure_days']}")
    print(f"Protein Failure Days: {weekly_metrics['protein_failure_days']}")
    print(f"Snack Usage Rate: {weekly_metrics['snack_usage_rate']}")
    print(f"Calorie Stability STD: {weekly_metrics['stability']['calorie_std']}")
    print(f"Protein Stability STD: {weekly_metrics['stability']['protein_std']}")


if __name__ == "__main__":
    main()