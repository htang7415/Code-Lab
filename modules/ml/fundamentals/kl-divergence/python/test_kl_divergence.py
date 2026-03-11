import math

import pytest

from kl_divergence import kl


def test_kl_is_zero_for_matching_distributions() -> None:
    assert abs(kl([0.5, 0.5], [0.5, 0.5])) < 1e-6


def test_kl_is_infinite_when_q_misses_positive_mass() -> None:
    assert math.isinf(kl([1.0, 0.0], [0.0, 1.0]))


def test_kl_validates_inputs() -> None:
    with pytest.raises(ValueError, match="same length"):
        kl([1.0], [1.0, 0.0])

    with pytest.raises(ValueError, match="non-negative"):
        kl([1.0, -0.1], [0.5, 0.5])
