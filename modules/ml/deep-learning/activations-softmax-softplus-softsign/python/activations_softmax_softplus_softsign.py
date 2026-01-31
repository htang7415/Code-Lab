import math


def softmax(row: list[float]) -> list[float]:
    m = max(row)
    exps = [math.exp(x - m) for x in row]
    s = sum(exps)
    return [e / s for e in exps]


def softplus(x: float) -> float:
    return math.log1p(math.exp(x))


def softsign(x: float) -> float:
    return x / (1 + abs(x))
