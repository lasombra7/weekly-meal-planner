import json
from db_connector import connect_db, load_user_profile
from calculator import calculate_targets
from meal_generator import generate_weekly_meal_plan
from strategies.registry import get_strategy
from explanation.daily_explainer import explain_daily_plan
from explanation.daily_metrics import evaluate_daily_plan
from explanation.weekly_evaluator import evaluate_weekly_plan


def generate_weekly_plan_for_user(
        user_id=None,
        visitor_profile=None,
        strategy_name="random",
):
    """
    支持两种模式：
        - User Mode: 通过 user_id 加载已保存的用户信息，并将生成的信息保存在user weekly plan
        - Visitor Mode: 使用临时传入的visitor_profile
    返回包含mode, user_profile, targets, strategy_name, weekly_plan的词典
    """

    # 第一步：获取用户信息
    if user_id is not None:
        profile = load_user_profile(user_id)
        mode = "user"
    else:
        if visitor_profile is None:
            raise ValueError("visitor mode requires visitor_profile input.")
        profile = visitor_profile
        mode = "visitor"

    # 第二步：根据用户信息计算目标
    target_cal, protein_range = calculate_targets(
        height_cm=profile["height_cm"],
        weight_kg=profile["weight_kg"],
        age=profile["age"],
        sex=profile["sex"],
        activity_level=profile["activity_level"],
        goal=profile["goal"]
    )
    if mode == "visitor":
        meal_structure = visitor_profile.get("meal_structure", "two_meals")
    else:
        meal_structure = profile.get("meal_structure", "two_meals")

    # 第三步：根据名称获取策略，如果为空则使用random strategy。当前阶段仅解析strategy，实际使用在后续阶段接入
    strategy = get_strategy(strategy_name)

    # 第四步：生成weekly meal plan （测试用）
    conn = connect_db()
    weekly_plan = generate_weekly_meal_plan(conn, target_cal=target_cal, protein_range=protein_range, meal_structure=meal_structure)
    conn.close()

    # 第五步：仅在user mode下保存weekly plan
    if mode == "user":
        save_weekly_plan(user_id, weekly_plan)

    # Phase 5 Integration
    daily_explanations = []
    daily_metrics_list = []
    for day in weekly_plan:
        explanation = explain_daily_plan(
            daily_plan=day,
            strategy_name=strategy_name,
            meal_structure=meal_structure,
            generation_attempts=None
        )
        metrics = evaluate_daily_plan(day)
        daily_explanations.append(explanation)
        daily_metrics_list.append(metrics)
    weekly_metrics = evaluate_weekly_plan(daily_metrics_list)

    return{
        "mode": mode,
        "user_profile": profile,
        "targets": {
            "calorie": target_cal,
            "protein_range": protein_range
        },
        "strategy_name": strategy_name,
        "weekly_plan": weekly_plan,

        # Phase 5 additions
        "daily_explanations": daily_explanations,
        "daily_metrics": daily_metrics_list,
        "weekly_metrics": weekly_metrics
    }

def save_weekly_plan(user_id, weekly_plan):
    """
    将生成的一周 meal plan 保存为用户的 weekly plan快照保存.
    """

    conn = connect_db()
    cursor = conn.cursor()

    sql = """
        INSERT INTO user_weekly_plan (user_id, plan_date, plan_json)
        VALUES (%s, CURDATE(), %s)
        ON DUPLICATE KEY UPDATE
            plan_json = VALUES(plan_json)
    """
    cursor.execute(
        sql,
        (
            user_id,
            json.dumps(weekly_plan, ensure_ascii=False)
        )
    )

    conn.commit()
    cursor.close()
    conn.close()

def load_latest_weekly_plan(user_id):
    """
    读取指定用户最近一次生成的weekly meal plan
    如果不存在则返回None
    """

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    sql = """
        SELECT plan_json, plan_date, created_at
        FROM user_weekly_plan
        WHERE user_id = %s
        ORDER BY plan_date DESC
        LIMIT 1
    """

    cursor.execute(sql, (user_id,))
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row is None:
        return None

    return {
        "plan_date": row["plan_date"],
        "created_at": row["created_at"],
        "weekly_plan": json.loads(row["plan_json"])
    }
