from db_connector import connect_db
from meal_generator import generate_weekly_meal_plan
from explanation.daily_explainer import explain_daily_plan
from explanation.daily_metrics import evaluate_daily_plan

conn = connect_db()
weekly_plan = generate_weekly_meal_plan(conn)
conn.close()
day = weekly_plan[0]

explanation = explain_daily_plan(
    daily_plan=day,
    strategy_name="random",
    meal_structure="two_meals",
    generation_attempts=None
)

metrics = evaluate_daily_plan(day)
print("====== EXPLANATION ======")
print(explanation)
print("====== METRICS ======")
print(metrics)