from __future__ import annotations


TRANSIENT_ERRORS = {"timeout", "rate_limit", "temporary_unavailable"}


def retry_action(error_type: str, attempt: int, max_attempts: int, idempotent: bool) -> str:
    if attempt < 0 or max_attempts <= 0:
        raise ValueError("attempt must be non-negative and max_attempts positive")

    normalized_error = error_type.strip().lower()
    if normalized_error in TRANSIENT_ERRORS and idempotent and attempt < max_attempts:
        return "retry"
    if normalized_error in TRANSIENT_ERRORS:
        return "fallback"
    return "fail-fast"


def retry_delay_ms(base_delay_ms: int, attempt: int, max_delay_ms: int) -> int:
    if base_delay_ms <= 0 or attempt < 0 or max_delay_ms < base_delay_ms:
        raise ValueError("invalid retry delay inputs")
    return min(max_delay_ms, base_delay_ms * (2 ** attempt))


def fallback_target(primary_path: str, fallback_map: dict[str, str] | None = None) -> str | None:
    if fallback_map is None:
        fallback_map = {
            "live-recommendations": "cached-recommendations",
            "semantic-search": "keyword-search",
            "llm-summary": "template-summary",
        }
    cleaned_path = primary_path.strip()
    if not cleaned_path:
        raise ValueError("primary_path must be non-empty")
    return fallback_map.get(cleaned_path)
