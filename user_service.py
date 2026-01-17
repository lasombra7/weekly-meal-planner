from db_connector import connect_db, load_user_profile
from calculator import calculate_targets
from meal_generator import generate_weekly_meal_plan
from strategies.registry import get_strategy


def generate_weekly_plan_for_user(
        user_id=None,
        visitor_profile=None,
        strategy_name="random",
):
    """
    支持两种模式：
    - User Mode: 通过 user_id 加载已保存的用户信息
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

    # 第三步：根据名称获取策略，如果为空则使用random strategy
    strategy = get_strategy(strategy_name)

    # 第四步：生成weekly meal plan （测试用）
    conn = connect_db()
    weekly_plan = generate_weekly_meal_plan(
        conn,
        target_cal=target_cal,
        protein_range=protein_range
    )
    conn.close()

    return{
        "mode": mode,
        "user_profile": profile,
        "targets": {
            "calorie": target_cal,
            "protein_range": protein_range
        },
        "strategy_name": strategy_name,
        "weekly_plan": weekly_plan
    }