import pytest

from eligibility_traces import eligibility_trace_step


def test_eligibility_trace_step_adds_current_feature_and_decayed_history() -> None:
    trace = eligibility_trace_step(previous_trace=0.5, feature_value=1.0, gamma=0.9, lam=0.8)

    assert trace == pytest.approx(1.36)


def test_eligibility_trace_step_decays_to_zero_without_feature_activation() -> None:
    trace = eligibility_trace_step(previous_trace=2.0, feature_value=0.0, gamma=0.5, lam=0.5)

    assert trace == pytest.approx(0.5)


def test_eligibility_trace_step_requires_valid_lambda() -> None:
    with pytest.raises(ValueError, match="lam"):
        eligibility_trace_step(previous_trace=0.0, feature_value=1.0, gamma=0.9, lam=1.5)
