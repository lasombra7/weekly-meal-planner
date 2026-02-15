from src.strategies.random_strategy import RandomStrategy
from src.strategies.greedy_strategy import GreedyStrategy
from src.strategies.weighted_strategy import WeightedStrategy


_STRATEGY_REGISTRY = {
    "random": RandomStrategy,
    "greedy": GreedyStrategy,
    "weighted": WeightedStrategy
}

def get_strategy(name: str):
    """
    根据名称返回对应的策略。
    如果名称不存在则抛出明确错误。
    """
    if name not in _STRATEGY_REGISTRY:
        raise ValueError(
            f"Unknown strategy '{name}'. "
            f"Available strategies: {list(_STRATEGY_REGISTRY.keys())}"
        )

    return _STRATEGY_REGISTRY[name]()