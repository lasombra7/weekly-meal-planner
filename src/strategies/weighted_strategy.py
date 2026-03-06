import random
from .base import MealStrategy


class WeightedStrategy(MealStrategy):
    """
    加权策略（蛋白质优先，但是保留多样性）
    核心思想：
    - 蛋白质的protein density 越高，被选中的概率越大。
    - 不再是100%选择最优选择，避免食物单一重复。
    The core idea of the greedy strategy (prioritizing proteins while maintaining diversity):
    - The higher the protein density, the greater the probability of being selected.
    - No longer 100% choosing the optimal option, to avoid repetitive and monotonous food choices.
    """
    name = "weighted"

    def pick_protein(self, proteins, context=None):
        """
        基于 protein density 的加权随机选择。
        Weighted random selection based on protein density.
        protein density = protein / calorie
        """

        def protein_density(item):
            calorie = item.get("calorie", 0)
            # 避免除零
            # Avoid division by zero
            if calorie <= 0:
                return 0
            return item.get("protein", 0) / calorie

        # 计算每个蛋白食物的权重
        # Calculate the weight of each protein food
        weights = [protein_density(p) for p in proteins]
        # 避免全是0的极端情况，退化为随机选择
        # Avoid extreme cases where everything is zero and degenerate into random selection
        if sum(weights) == 0:
            return random.choice(proteins)

        # 加权随机选择一个
        # Weighted random selection of one
        return random.choices(proteins, weights=weights, k=1)[0]

    def pick_main(self, mains, context=None):
        # 主食暂时不加权
        # No weighted strategy for main items for now
        return random.choice(mains)

    def pick_vegetable(self, vegetables, context=None):
        # 蔬菜暂时不加权
        # No weighted strategy for vegetable items for now
        return random.choice(vegetables)