from __future__ import annotations

import math


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def dynamic_tanh(
    x: float,
    alpha: float = 1.0,
    gamma: float = 1.0,
    beta: float = 0.0,
) -> float:
    return gamma * math.tanh(alpha * x) + beta


def softmax(row: list[float]) -> list[float]:
    if not row:
        raise ValueError("row must be non-empty")
    maximum = max(row)
    exps = [math.exp(value - maximum) for value in row]
    total = sum(exps)
    return [value / total for value in exps]


def scalar_activations(x: float, alpha: float = 0.01) -> dict[str, float]:
    if alpha < 0.0:
        raise ValueError("alpha must be non-negative")

    sigmoid_value = sigmoid(x)
    swiglu_gate = sigmoid(x)
    return {
        "sigmoid": sigmoid_value,
        "tanh": math.tanh(x),
        "hard_sigmoid": max(0.0, min(1.0, 0.2 * x + 0.5)),
        "hardtanh": max(-1.0, min(1.0, x)),
        "dynamic_tanh": dynamic_tanh(x, alpha=1.2, gamma=1.0, beta=0.0),
        "relu": max(0.0, x),
        "leaky_relu": x if x > 0.0 else alpha * x,
        "elu": x if x > 0.0 else alpha * (math.exp(x) - 1.0),
        "prelu": x if x > 0.0 else alpha * x,
        "swish": x * sigmoid_value,
        "gelu": 0.5 * x * (1.0 + math.tanh(math.sqrt(2.0 / math.pi) * (x + 0.044715 * x**3))),
        "mish": x * math.tanh(math.log1p(math.exp(x))),
        "swiglu": x * swiglu_gate * x,
        "softplus": math.log1p(math.exp(x)),
        "softsign": x / (1.0 + abs(x)),
    }
