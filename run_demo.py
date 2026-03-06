from src.core.user_service import generate_weekly_plan_for_user

def print_meal_items(meal_items):
    # 打印单顿主餐里的食物信息
    for category, item in meal_items.items():
        name = item["name"]
        grams = item.get("grams", 100)
        calorie = item["calorie_per_100g"]
        protein = item["protein_pre_100g"]
        print(f"    - {category.capitalize()}: {name} ({grams}g, {calorie} kcal/100g, {protein} g protein/100g)")