def beta_posterior(alpha: float, beta: float, successes: int, failures: int) -> tuple[float, float]:
    return alpha + successes, beta + failures
