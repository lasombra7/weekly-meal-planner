import random
from .base import MealStrategy


class RandomStrategy(MealStrategy):
    """
    随机策略Random Strategy（baseline）：
    行为等同于Phase 2 中的random.choice逻辑
    """
    name = "random"

    def pick_main(self, mains, context=None):
        return random.choice(mains)
    def pick_protein(self, proteins, context=None):
        return  random.choice(proteins)
    def pick_vegetable(self, vegetables, context=None):
        return random.choice(vegetables)