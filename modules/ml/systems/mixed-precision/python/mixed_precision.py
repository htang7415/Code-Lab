def scale_gradients(grads: list[float], scale: float) -> list[float]:
    return [g * scale for g in grads]
