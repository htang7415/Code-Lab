from __future__ import annotations


def _matvec(w: list[list[float]], x: list[float]) -> list[float]:
    return [sum(w_row[j] * x[j] for j in range(len(x))) for w_row in w]


def _relu(x: list[float]) -> list[float]:
    return [max(0.0, v) for v in x]


def feedforward(
    x: list[float],
    weights: list[list[list[float]]],
    biases: list[list[float]],
) -> list[float]:
    h = x
    for w, b in zip(weights, biases):
        h = [v + b[i] for i, v in enumerate(_matvec(w, h))]
        h = _relu(h)
    return h
