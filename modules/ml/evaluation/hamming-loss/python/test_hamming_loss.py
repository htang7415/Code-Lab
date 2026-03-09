import pytest

from hamming_loss import hamming_loss


def test_hamming_loss_counts_labelwise_mismatches() -> None:
    loss = hamming_loss(predictions=[[1, 0, 1], [0, 1, 0]], labels=[[1, 1, 1], [0, 0, 0]])

    assert loss == pytest.approx(2.0 / 6.0)


def test_hamming_loss_is_zero_for_exact_match() -> None:
    assert hamming_loss(predictions=[[1, 0]], labels=[[1, 0]]) == pytest.approx(0.0)


def test_hamming_loss_requires_binary_values() -> None:
    with pytest.raises(ValueError, match="binary"):
        hamming_loss(predictions=[[2]], labels=[[1]])
