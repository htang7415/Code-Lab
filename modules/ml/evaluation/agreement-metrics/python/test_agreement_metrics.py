import pytest

from agreement_metrics import agreement_rate, cohen_kappa


def test_agreement_rate_returns_modal_share() -> None:
    assert agreement_rate(["yes", "yes", "no"]) == pytest.approx(2 / 3)


def test_cohen_kappa_is_positive_when_diagonal_dominates() -> None:
    assert cohen_kappa([[8, 2], [1, 9]]) > 0.0


def test_invalid_confusion_matrix_raises() -> None:
    with pytest.raises(ValueError, match="square"):
        cohen_kappa([[1, 2]])
