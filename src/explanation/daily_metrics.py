def evaluate_daily_plan(daily_plan: dict) -> dict:
    """
    对单日 meal plan 进行客观评估，生成 evaluation metric。
    注意：不修改meal plan，不生成解释文本，不做主观评价，只输出可量化指标。
    """

    target = daily_plan["target"]
    total_calorie = daily_plan["total_calorie"]
    total_protein = daily_plan["total_protein"]

    target_calorie = target["calorie"]
    protein_lower_bound = target["protein_lower_bound"]
    protein_upper_bound = target["protein_upper_bound"]

    # 第一步 偏差计算（绝对量）
    calorie_deviation = total_calorie - target_calorie
    protein_deviation = total_protein - protein_lower_bound

    # 第二步：区间判断
    within_calorie_range = abs(calorie_deviation) <= 100
    within_protein_range = (protein_lower_bound <= total_protein <= protein_upper_bound)

    # 第三步：snack 使用情况
    snack_allowed = daily_plan.get("snack_allowed", False)

    # 第四步：constraint 归一化（数值越小，表示越贴近目标）
    calorie_tightness = abs(calorie_deviation) / target_calorie
    protein_range_width = max(protein_upper_bound - protein_lower_bound, 1)
    protein_tightness = abs(total_protein - protein_lower_bound) / protein_range_width

    # 第五步：assemble metrics
    metrics = {
        "calorie_deviation": round(calorie_deviation, 1),
        "protein_deviation": round(protein_deviation, 1),
        "within_calorie_range": within_calorie_range,
        "within_protein_range": within_protein_range,
        "snack_allowed": snack_allowed,
        "constraint_tightness":{
            "calorie": round(calorie_tightness, 3),
            "protein": round(protein_tightness, 3)
        }
    }

    return metrics