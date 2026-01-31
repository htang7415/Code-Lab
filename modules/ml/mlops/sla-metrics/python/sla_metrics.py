def violation_rate(violations: int, total: int) -> float:
    return violations / total if total > 0 else 0.0
