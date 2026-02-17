from src.db.db_connector import connect_db
from src.strategies.registry import get_strategy
from src.core.meal_generator import generate_weekly_meal_plan, generate_main_meal


conn = connect_db()

def print_main_meal(meal):
    print(f"\n{meal['type'].title()}")
    print("-" * 60)

    for category, item in meal["meal_items"].items():
        grams = item["grams"]
        real_cal = item["calorie_per_100g"] / 100 * grams
        real_protein = item["protein_per_100g"] / 100 * grams
        print(
            f"  -  {category.title()}: {item['name']} "
            f"({grams} g | "
            f"{round(real_cal, 1)} kcal | "
            f"{round(real_protein, 1)} g protein)"
        )

    print(f"  →  Total:{meal['total_calorie']} kcal, {meal['total_protein']} g protein \n")

# ===== 原 Weekly 逻辑 =====
print("=== Weekly Plan (Default: Random Strategy) ===")
weekly_plan = generate_weekly_meal_plan(conn, meal_structure="two_meals")
for day in weekly_plan:
    print(f"Day {day['day']} - {day['total_calorie']} kcal / {day['total_protein']} g protein |")
    print(f"Snack allowed: {day['snack_allowed']}")
    print("-" * 60)

    # 打印每顿主餐详情
    for meal in day["meals"]:
        print_main_meal(meal)

    # 如果有snack，打印snack详情
    snack = day["snack_option"]
    print(f"Snack option({'Allowed' if day['snack_allowed'] else 'Optional only'}):")
    for category, item in snack["items"].items():
        print(f"  -  {category.title()}: {item['name']} ({item['calorie_per_100g']} kcal, {item['protein_per_100g']} g protein)")
    print(f"  →  Total:{snack['total_calorie']} kcal, {snack['total_protein']} g protein")
    print("=" * 60)

# ===== 现测试Greedy Strategy =====
print("\n=== Greedy Strategy Test ===")
meal = generate_main_meal(conn, calorie_target=850, protein_range=(60,75), strategy=get_strategy("greedy"))
print_main_meal(meal)

# ===== 现测试Weighted Strategy =====
print("=== Weighted Strategy Test ===")
meal = generate_main_meal(conn, calorie_target=850, protein_range=(60,75), strategy=get_strategy("weighted"))
print_main_meal(meal)

conn.close()