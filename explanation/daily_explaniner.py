def explain_daily_plan(
        daily_plan: dict,
        strategy_name: str,
        meal_structure: str,
        generation_attempts: int | None = None
):
    """
    为单日meal plan 生成 explainable metadata。
    注意：不修改daily_plan,不重新计算，只解释发生了什么
    """

    target = daily_plan["target"]
    total_calorie = daily_plan["total_calorie"]
    total_protein = daily_plan["total_protein"]

    # 第一步：识别binding constraints
    binding_constraints = []
    if total_calorie < target["calorie"]:
        binding_constraints.append("calorie_lower_bound")
    elif total_calorie > target["calorie"]:
        binding_constraints.append("calorie_upper_bound")

    if total_protein < target["protein_lower_bound"]:
        binding_constraints.append("protein_lower_bound")
    elif total_protein > target["protein_upper_bound"]:
        binding_constraints.append("protein_upper_bound")

    # 第二步：snake decision explain
    snack_allowed = daily_plan["snack_allowed"]
    if total_calorie < target["calorie"]:
        snack_reason = "main_meals_below_calorie_target"
        snack_considered = True
    else:
        snack_reason = "main_meals_meet_calorie_target"
        snack_considered = False

    snack_explanation = {
        "considered": snack_considered,
        "allowed": snack_allowed,
        "reason": snack_reason
    }

    # 第三步：Assemble explanation
    explanation = {
        "strategy": strategy_name,
        "meal_structure": meal_structure,
        "targets":{
            "calorie": target["calorie"],
            "protein_lower_bound": target["protein_lower_bound"],
            "protein_upper_bound": target["protein_upper_bound"]
        },
        "actual":{
            "total_calorie": total_calorie,
            "total_protein": total_protein
        },
        "binding_constraints": binding_constraints,
        "snack_decision": snack_explanation,
        "generation_stats":{
            "attempts": generation_attempts
        }
    }

    return explanation