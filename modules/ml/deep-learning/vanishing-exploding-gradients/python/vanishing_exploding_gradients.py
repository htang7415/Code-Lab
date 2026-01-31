def gradient_chain(weights: list[float], grad: float = 1.0) -> float:
    out = grad
    for w in weights:
        out *= w
    return out
