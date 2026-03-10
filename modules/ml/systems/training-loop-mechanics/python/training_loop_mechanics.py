from __future__ import annotations

import math


def zero_grad(grads: list[float]) -> list[float]:
    return [0.0 for _ in grads]


def forward(x: list[float], w: list[float], b: float) -> float:
    if len(x) != len(w):
        raise ValueError("x and w must have the same length")
    return sum(wi * xi for wi, xi in zip(w, x)) + b


def backward(dy: float, x: float) -> float:
    return dy * x


def step(w: float, grad: float, lr: float) -> float:
    return w - lr * grad


def accumulate(grads: list[list[float]]) -> list[float]:
    if not grads:
        return []
    total = [0.0 for _ in grads[0]]
    for grad in grads:
        total = [left + right for left, right in zip(total, grad)]
    return total


def scale_gradients(grads: list[float], scale: float) -> list[float]:
    return [gradient * scale for gradient in grads]


def gradients_ok(grads: list[float]) -> bool:
    if any(math.isnan(gradient) for gradient in grads):
        return False
    return any(abs(gradient) > 0 for gradient in grads)
