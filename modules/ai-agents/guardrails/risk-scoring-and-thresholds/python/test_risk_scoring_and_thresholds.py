from __future__ import annotations

import pytest

from risk_scoring_and_thresholds import (
    active_risk_signals,
    risk_decision,
    weighted_risk_score,
)


def test_risk_scoring_and_thresholds_aggregate_signals_and_decide() -> None:
    signals = {
        "untrusted_input": 0.90,
        "side_effect": 0.80,
        "secret_access": 0.20,
    }
    weights = {
        "untrusted_input": 0.40,
        "side_effect": 0.40,
        "secret_access": 0.20,
    }

    assert weighted_risk_score(signals, weights) == pytest.approx(0.72)
    assert active_risk_signals(signals, min_signal=0.70) == [
        "side_effect",
        "untrusted_input",
    ]
    assert risk_decision(0.72, review_threshold=0.50, block_threshold=0.80) == "review"
    assert risk_decision(0.85, review_threshold=0.50, block_threshold=0.80) == "block"
    assert risk_decision(0.30, review_threshold=0.50, block_threshold=0.80) == "allow"


def test_risk_scoring_and_thresholds_validation() -> None:
    with pytest.raises(ValueError):
        weighted_risk_score({}, {"side_effect": 1.0})
    with pytest.raises(ValueError):
        weighted_risk_score({"side_effect": 0.5}, {})
    with pytest.raises(ValueError):
        weighted_risk_score({"side_effect": 1.2}, {"side_effect": 1.0})
    with pytest.raises(ValueError):
        active_risk_signals({"side_effect": 0.5}, min_signal=1.1)
    with pytest.raises(ValueError):
        risk_decision(0.5, review_threshold=0.9, block_threshold=0.8)
