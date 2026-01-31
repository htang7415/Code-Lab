import math


def dynamic_tanh(x: float, alpha: float = 1.0, gamma: float = 1.0, beta: float = 0.0) -> float:
    """Dynamic Tanh (DyT): gamma * tanh(alpha * x) + beta."""
    return gamma * math.tanh(alpha * x) + beta


def activations(x: float) -> dict[str, float]:
    sigmoid = 1 / (1 + math.exp(-x))
    tanh = math.tanh(x)
    hard_sigmoid = max(0.0, min(1.0, 0.2 * x + 0.5))
    hardtanh = max(-1.0, min(1.0, x))
    dynamic = dynamic_tanh(x, alpha=1.2, gamma=1.0, beta=0.0)
    return {
        "sigmoid": sigmoid,
        "tanh": tanh,
        "hard_sigmoid": hard_sigmoid,
        "hardtanh": hardtanh,
        "dynamic_tanh": dynamic,
    }
