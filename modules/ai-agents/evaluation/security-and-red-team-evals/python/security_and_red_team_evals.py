from __future__ import annotations


DEFAULT_HIGH_RISK_LABELS = [
    "prompt_injection",
    "data_exfiltration",
    "privilege_escalation",
    "unsafe_action",
]


def security_eval_breakdown(failed_attack_types: list[str]) -> dict[str, int]:
    if not failed_attack_types:
        raise ValueError("failed_attack_types must be non-empty")

    breakdown: dict[str, int] = {}
    for attack_type in failed_attack_types:
        cleaned = attack_type.strip().lower()
        if not cleaned:
            raise ValueError("attack types must be non-empty")
        breakdown[cleaned] = breakdown.get(cleaned, 0) + 1
    return breakdown


def high_risk_failure_count(
    breakdown: dict[str, int],
    high_risk_labels: list[str] | None = None,
) -> int:
    if not breakdown:
        raise ValueError("breakdown must be non-empty")

    labels = high_risk_labels or DEFAULT_HIGH_RISK_LABELS
    high_risk = {label.strip().lower() for label in labels if label.strip()}
    return sum(count for label, count in breakdown.items() if label in high_risk)


def security_release_gate(pass_rate: float, high_risk_failures: int, min_pass_rate: float) -> str:
    if not 0.0 <= pass_rate <= 1.0:
        raise ValueError("pass_rate must satisfy 0 <= value <= 1")
    if not 0.0 <= min_pass_rate <= 1.0:
        raise ValueError("min_pass_rate must satisfy 0 <= value <= 1")
    if high_risk_failures < 0:
        raise ValueError("high_risk_failures must be non-negative")

    if high_risk_failures > 0:
        return "fail"
    if pass_rate < min_pass_rate:
        return "review"
    return "pass"
