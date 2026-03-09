import math

import pytest

from log_loss import log_loss


def test_log_loss_matches_binary_cross_entropy() -> None:
    score = log_loss(labels=[1, 0], probabilities=[0.8, 0.2])

    assert score == pytest.approx(-0.5 * (math.log(0.8) + math.log(0.8)))


def test_log_loss_penalizes_confident_wrong_predictions() -> None:
    mild = log_loss(labels=[1], probabilities=[0.6])
    severe = log_loss(labels=[1], probabilities=[0.01])

    assert severe > mild


def test_log_loss_requires_positive_eps() -> None:
    with pytest.raises(ValueError, match="positive"):
        log_loss(labels=[1], probabilities=[0.5], eps=0.0)
