def calculate_targets(height_cm, weight_kg, age, sex="female", activity_level="moderate", goal="maintain"):
    """
    根据基础信息计算每日target_cal和protein范围。
    """
    # Mifflin–St Jeor BMR formula
    if sex == "female":  # 女性
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    else:  # 男性
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5

    activity_factor_map = {
        "low": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "high": 1.725
    }
    factor = activity_factor_map.get(activity_level, 1.55)
    tdee = bmr * factor

    # 根据目标微调（基础版本）
    if goal == "lose":
        target_cal = round(tdee - 300)
    elif goal == "gain":
        target_cal = round(tdee + 200)
    else:
        target_cal = round(tdee)

    # 蛋白质：按照每公斤1.6g - 2.0g 粗略的给一个区间
    protein_lower_bound = round(weight_kg * 1.6)
    protein_upper_bound = round(weight_kg * 2.0)

    return target_cal, (protein_lower_bound, protein_upper_bound)