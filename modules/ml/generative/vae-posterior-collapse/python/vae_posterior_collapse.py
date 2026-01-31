def kl_is_low(kl: float, threshold: float = 0.1) -> bool:
    return kl < threshold
