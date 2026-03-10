from __future__ import annotations

import math


def neuron(x: list[float], w: list[float], b: float) -> float:
    z = sum(weight * value for weight, value in zip(w, x)) + b
    return 1.0 / (1.0 + math.exp(-z))


def _matvec(weights: list[list[float]], x: list[float]) -> list[float]:
    return [sum(row[index] * x[index] for index in range(len(x))) for row in weights]


def _relu(x: list[float]) -> list[float]:
    return [max(0.0, value) for value in x]


def feedforward(
    x: list[float],
    weights: list[list[list[float]]],
    biases: list[list[float]],
) -> list[float]:
    hidden = x
    for weight_matrix, bias_vector in zip(weights, biases):
        hidden = [value + bias_vector[index] for index, value in enumerate(_matvec(weight_matrix, hidden))]
        hidden = _relu(hidden)
    return hidden
