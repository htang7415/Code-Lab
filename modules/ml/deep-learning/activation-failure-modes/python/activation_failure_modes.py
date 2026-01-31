def dead_relu_fraction(values: list[float]) -> float:
    if not values:
        return 0.0
    dead = sum(1 for v in values if v <= 0.0)
    return dead / len(values)
