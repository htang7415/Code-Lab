def conversion_rate(conversions: int, trials: int) -> float:
    return conversions / trials if trials > 0 else 0.0
