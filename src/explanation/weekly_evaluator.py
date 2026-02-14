import math

def evaluate_weekly_plan(daily_metrics_list: list[dict]) -> dict:
    """
    对一周的 daily_metrics 进行评估。
    """

    if not daily_metrics_list:
        raise ValueError("daily_metrics_list cannot be empty")

    days = len(daily_metrics_list)

    # 第一步：平均偏差
    avg_calorie_deviation = sum(d["calorie_deviation"] for d in daily_metrics_list) / days
    avg_protein_deviation = sum(d["protein_deviation"] for d in daily_metrics_list) / days

    # 第二步：失败天数统计
    calorie_failure_days = sum(not d["within_calorie_range"] for d in daily_metrics_list)
    protein_failure_days = sum(not d["within_protein_range"] for d in daily_metrics_list)

    # 第三步：snack 使用率
    snack_days = sum(d.get("snack_allowed", False) for d in daily_metrics_list)
    snack_usage_rate = snack_days / days

    # 第四步：稳定性（标准差）
    calorie_devs = [d["calorie_deviation"] for d in daily_metrics_list]
    protein_devs = [d["protein_deviation"] for d in daily_metrics_list]
    calorie_mean = avg_calorie_deviation
    protein_mean = avg_protein_deviation
    calorie_std = math.sqrt(sum((x - calorie_mean) ** 2 for x in calorie_devs) / days)
    protein_std = math.sqrt(sum((x - protein_mean) ** 2 for x in protein_devs) / days)

    # 第五步： assemble weekly metrics
    weekly_metrics = {
        "avg_calorie_deviation": round(avg_calorie_deviation, 1),
        "avg_protein_deviation": round(avg_protein_deviation, 1),
        "calorie_failure_days": calorie_failure_days,
        "protein_failure_days": protein_failure_days,
        "snack_usage_rate": round(snack_usage_rate, 2),
        "stability":{
            "calorie_std": round(calorie_std, 2),
            "protein_std": round(protein_std, 2)
        }
    }

    return weekly_metrics
