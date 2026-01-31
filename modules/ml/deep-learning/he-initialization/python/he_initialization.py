import math


def he_normal(fan_in: int, fan_out: int, seed: int = 0) -> list[float]:
    std = math.sqrt(2 / fan_in)
    # Box-Muller with deterministic LCG
    values = []
    state = seed
    for _ in range(fan_in * fan_out // 2 + 1):
        state = (1103515245 * state + 12345) % (2**31)
        u1 = (state / (2**31 - 1)) or 1e-6
        state = (1103515245 * state + 12345) % (2**31)
        u2 = state / (2**31 - 1)
        z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        z1 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
        values.extend([z0 * std, z1 * std])
    return values[: fan_in * fan_out]
