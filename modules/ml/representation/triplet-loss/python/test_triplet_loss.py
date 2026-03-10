import pytest

from triplet_loss import triplet_loss


def test_triplet_loss_is_zero_when_margin_is_satisfied() -> None:
    assert triplet_loss(0.3, 0.8, margin=0.2) == pytest.approx(0.0)


def test_triplet_loss_is_positive_when_negative_is_too_close() -> None:
    assert triplet_loss(0.4, 0.5, margin=0.2) == pytest.approx(0.1)


def test_triplet_loss_requires_non_negative_distances() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        triplet_loss(-0.1, 0.5)
