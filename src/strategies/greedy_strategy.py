import random
from .base import MealStrategy


class GreedyStrategy(MealStrategy):
    """
    贪心策略（蛋白质优先）
    核心思想：
    - 在蛋白的选择上优先选择protein / calorie比值最高的食材。
    - 其他类别（主食、蔬菜）暂时保持随机，避免过度复杂。
    The core idea of the greedy strategy (protein first):
    - In the selection of protein, prioritize ingredients with the highest protein/calorie ratio.
    - For other categories (staple foods, vegetables), keep them random for the time being to avoid excessive complexity.
    """
    name = "greedy"

    def pick_protein(self, proteins, context=None):
        """
        从蛋白质列表中选择protein density 最高的食材。
        Select the ingredient with the highest protein density from the protein list.
        protein density = protein / calorie
        """

        def protein_density(item):
            calorie = item.get("calorie", 0)
            # 避免除零
            # Avoid division by zero
            if calorie <= 0:
                return 0
            return item.get("protein", 0) / calorie

        # 按照protein density 从高到低排序，选择排名第一的
        # Sort by protein density from high to low and select the one ranked first
        sorted_proteins = sorted(
            proteins,
            key=protein_density,
            reverse=True
        )
        return sorted_proteins[0]

    def pick_main(self, mains, context=None):
        # 主食暂时不贪心
        # No greedy strategy for main items for now
        return random.choice(mains)

    def pick_vegetable(self, vegetables, context=None):
        # 蔬菜暂时不贪心
        # No greedy strategy for vegetable items for now
        return  random.choice(vegetables)