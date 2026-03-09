import pytest

from temperature_sampling import temperature_probabilities


def test_temperature_probabilities_match_softmax_at_temperature_one() -> None:
    probabilities = temperature_probabilities([1.0, 0.0], temperature=1.0)

    assert probabilities == pytest.approx([0.7310585786300049, 0.2689414213699951])


def test_temperature_probabilities_get_sharper_with_lower_temperature() -> None:
    probabilities = temperature_probabilities([1.0, 0.0], temperature=0.5)

    assert probabilities == pytest.approx([0.8807970779778823, 0.11920292202211755])


def test_temperature_probabilities_requires_positive_temperature() -> None:
    with pytest.raises(ValueError, match="positive"):
        temperature_probabilities([1.0], temperature=0.0)
