import math


def reward_model_loss(chosen: float, rejected: float) -> float:
    diff = chosen - rejected
    return -math.log(1 / (1 + math.exp(-diff)))
