def newton_step(x: float, f_prime: float, f_double_prime: float) -> float:
    return x - f_prime / f_double_prime
