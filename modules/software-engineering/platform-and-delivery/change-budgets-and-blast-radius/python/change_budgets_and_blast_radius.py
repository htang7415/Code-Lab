from __future__ import annotations


def blast_radius(users_affected_percent: int, touches_write_path: bool, multi_region: bool) -> str:
    score = 0
    if users_affected_percent >= 25:
        score += 1
    if touches_write_path:
        score += 1
    if multi_region:
        score += 1
    if score >= 2:
        return "high"
    if score == 1:
        return "medium"
    return "low"


def change_budget_available(open_high_risk_changes: int, oncall_load: str) -> bool:
    normalized_load = oncall_load.strip().lower()
    if normalized_load not in {"low", "medium", "high"}:
        raise ValueError("unknown oncall_load")
    if normalized_load == "high":
        return False
    return open_high_risk_changes == 0


def progressive_delivery_required(radius: str, budget_available: bool) -> bool:
    return radius in {"medium", "high"} or not budget_available
