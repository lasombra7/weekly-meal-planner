from src.db.db_connector import connect_db
from src.core.meal_generator import generate_weekly_meal_plan
from src.explanation.daily_explainer import explain_daily_plan
from src.explanation.daily_metrics import evaluate_daily_plan
from src.explanation.weekly_evaluator import evaluate_weekly_plan

conn = connect_db()

try:
    weekly_plan = generate_weekly_meal_plan(conn)

    # 生成一周计划
    print("\n========== DAILY TEST ==========\n")

    daily_metrics_list = []

    for i, day in enumerate(weekly_plan, start=1):
        explanation = explain_daily_plan(
            daily_plan=day,
            strategy_name="random",
            meal_structure="two_meals",
            generation_attempts=None
        )

        metrics = evaluate_daily_plan(day)
        daily_metrics_list.append(metrics)

        print(f"\n====== Day{i} ======")
        print("====== EXPLANATION ======")
        print(explanation)
        print("====== METRICS ======")
        print(metrics)

    # Weekly 聚合
    print("\n========== WEEKLY TEST ==========\n")
    weekly_metrics = evaluate_weekly_plan(daily_metrics_list)
    print("====== Weekly Metrics ======")
    print(weekly_metrics)

finally:
    conn.close()