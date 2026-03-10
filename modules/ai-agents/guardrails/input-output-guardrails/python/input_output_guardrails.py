from __future__ import annotations


def blocked_by_terms(text: str, blocked_terms: list[str]) -> bool:
    lowered = text.lower()
    return any(term.strip().lower() in lowered for term in blocked_terms if term.strip())


def required_fields_present(record: dict[str, object], required_keys: list[str]) -> bool:
    return all(key in record for key in required_keys)


def should_escalate(model_confidence: float, threshold: float, blocked: bool) -> bool:
    if not 0.0 <= model_confidence <= 1.0:
        raise ValueError("model_confidence must satisfy 0 <= value <= 1")
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("threshold must satisfy 0 <= value <= 1")
    return blocked or model_confidence < threshold
