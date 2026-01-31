def relu_family(x: float, alpha: float = 0.01) -> dict[str, float]:
    relu = max(0.0, x)
    leaky = x if x > 0 else alpha * x
    elu = x if x > 0 else alpha * (pow(2.718281828, x) - 1)
    prelu = x if x > 0 else alpha * x
    return {"relu": relu, "leaky_relu": leaky, "elu": elu, "prelu": prelu}
