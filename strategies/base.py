class MealStrategy:
    """
    用于指定饮食选择策略的基类。
    策略决定的是食物的选择方式，而不是合适生成食物或者生成多少餐食。
    """
    name = "base"

    def pick_main(self, mains, context=None):
        raise NotImplementedError
    def pick_protein(self, proteins, context=None):
        raise NotImplementedError
    def pick_vegetable(self, vegetables, context=None):
        raise  NotImplementedError