def calculate_targets(height_cm, weight_kg, age, sex="female", activity_level="moderate", goal="maintain"):
    """
    根据基础信息计算每日target_cal和protein范围。
    """

    # 统一数据类型
    height_cm = float(height_cm)
    weight_kg = float(weight_kg)
    age = int(age)

    # 统一字符串类型
    sex = sex.lower()
    activity_level = activity_level.lower()
    goal = goal.lower()

    # Mifflin–St Jeor BMR formula
    if sex == "female":  # 女性
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    elif sex == "male":  # 男性
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        raise ValueError(f"Invalid sex value: {sex}. Must be 'male' or 'female'.")

    activity_factor_map = {
        "low": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "high": 1.725
    }
    if activity_level not in activity_factor_map:
        raise ValueError(f"Invalid activity_level value:{activity_level}. Must be one of {list(activity_factor_map.keys())}")
    factor = activity_factor_map[activity_level]
    tdee = bmr * factor

    # 根据目标微调（基础版本）
    if goal == "lose":
        target_cal = round(tdee - 300)
    elif goal == "maintain":
        target_cal = round(tdee)
    elif goal == "gain":
        target_cal = round(tdee + 200)
    else:
        raise ValueError(f"Invalid goal value:{goal}. Must be one of 'lose', 'maintain' or 'gain'.")

    # 蛋白质：按照每公斤1.6g - 2.0g 粗略的给一个区间
    protein_lower_bound = round(weight_kg * 1.6)
    protein_upper_bound = round(weight_kg * 2.0)

    return target_cal, (protein_lower_bound, protein_upper_bound)