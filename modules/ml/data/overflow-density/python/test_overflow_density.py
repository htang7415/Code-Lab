import pytest

from overflow_density import overflow_density


def test_overflow_density_normalizes_overflow_by_batch_size_and_cap() -> None:
    score = overflow_density([64, 120, 80, 200], max_length=100)

    assert score == pytest.approx(120 / 400)


def test_overflow_density_returns_zero_for_empty_input() -> None:
    assert overflow_density([], max_length=64) == pytest.approx(0.0)


def test_overflow_density_requires_positive_cap() -> None:
    with pytest.raises(ValueError, match="positive"):
        overflow_density([10], max_length=0)
