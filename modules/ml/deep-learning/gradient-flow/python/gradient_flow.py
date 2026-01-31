def propagate_variance(var: float, layer_vars: list[float]) -> float:
    out = var
    for v in layer_vars:
        out *= v
    return out
