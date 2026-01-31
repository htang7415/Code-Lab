import math


def preference_loss(score_chosen: float, score_rejected: float) -> float:
    diff = score_chosen - score_rejected
    return -math.log(1 / (1 + math.exp(-diff)))
