import math


def add_noise(x: float, noise: float, alpha: float) -> float:
    return math.sqrt(alpha) * x + math.sqrt(1 - alpha) * noise
