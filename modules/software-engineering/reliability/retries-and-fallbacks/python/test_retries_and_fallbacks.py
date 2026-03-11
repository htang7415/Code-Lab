from __future__ import annotations

import pytest

from retries_and_fallbacks import fallback_target, retry_action, retry_delay_ms


def test_retry_action_prefers_idempotent_transient_operations() -> None:
    assert retry_action("timeout", attempt=1, max_attempts=3, idempotent=True) == "retry"
    assert retry_action("timeout", attempt=3, max_attempts=3, idempotent=True) == "fallback"
    assert retry_action("timeout", attempt=1, max_attempts=3, idempotent=False) == "fallback"
    assert retry_action("validation_error", attempt=1, max_attempts=3, idempotent=True) == "fail-fast"


def test_retry_delay_is_exponential_and_capped() -> None:
    assert retry_delay_ms(base_delay_ms=200, attempt=0, max_delay_ms=1000) == 200
    assert retry_delay_ms(base_delay_ms=200, attempt=3, max_delay_ms=1000) == 1000


def test_fallback_target_returns_known_degraded_path() -> None:
    assert fallback_target("live-recommendations") == "cached-recommendations"
    assert fallback_target("unknown-path") is None

    with pytest.raises(ValueError):
        fallback_target(" ")
