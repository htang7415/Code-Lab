import math


def cross_entropy(logits: list[float], target: int) -> float:
    m = max(logits)
    exps = [math.exp(x - m) for x in logits]
    s = sum(exps)
    prob = exps[target] / s
    return -math.log(prob)
