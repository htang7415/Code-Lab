from __future__ import annotations


def propagate_variance(var: float, layer_vars: list[float]) -> float:
    out = var
    for layer_var in layer_vars:
        out *= layer_var
    return out


def gradient_chain(weights: list[float], grad: float = 1.0) -> float:
    out = grad
    for weight in weights:
        out *= weight
    return out
