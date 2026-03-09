import pytest

from first_visit_monte_carlo_prediction import first_visit_returns


def test_first_visit_returns_uses_first_occurrence_of_each_state() -> None:
    returns = first_visit_returns(
        states=["A", "B", "A"],
        rewards=[1.0, 2.0, 3.0],
        gamma=1.0,
    )

    assert returns == {"B": 5.0, "A": 6.0}


def test_first_visit_returns_applies_discounting() -> None:
    returns = first_visit_returns(
        states=["A", "B"],
        rewards=[2.0, 4.0],
        gamma=0.5,
    )

    assert returns == {"B": 4.0, "A": 4.0}


def test_first_visit_returns_requires_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        first_visit_returns(["A"], [1.0, 2.0], gamma=0.9)
