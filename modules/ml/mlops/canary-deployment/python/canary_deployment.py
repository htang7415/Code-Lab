def split_traffic(total: int, canary_pct: float) -> tuple[int, int]:
    canary = int(total * canary_pct)
    return canary, total - canary
