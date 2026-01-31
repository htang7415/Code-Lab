import math


def xavier_uniform(fan_in: int, fan_out: int, seed: int = 0) -> list[float]:
    limit = math.sqrt(6 / (fan_in + fan_out))
    # simple LCG for deterministic demo
    values = []
    state = seed
    for _ in range(fan_in * fan_out):
        state = (1103515245 * state + 12345) % (2**31)
        values.append(-limit + (state / (2**31 - 1)) * (2 * limit))
    return values
