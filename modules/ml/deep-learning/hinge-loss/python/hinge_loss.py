def hinge_loss(score: float, label: int) -> float:
    return max(0.0, 1 - label * score)
