import math

import pytest

from activation_functions import dynamic_tanh, scalar_activations, softmax


def test_scalar_activations_cover_multiple_families() -> None:
    out = scalar_activations(-2.0, alpha=0.1)

    assert out["relu"] == 0.0
    assert out["leaky_relu"] < 0.0
    assert 0.0 <= out["sigmoid"] <= 1.0
    assert -1.0 <= out["tanh"] <= 1.0
    assert "gelu" in out
    assert "softplus" in out


def test_softmax_returns_normalized_distribution() -> None:
    row = softmax([1.0, 1.0, 2.0])

    assert sum(row) == pytest.approx(1.0)
    assert row[2] > row[0]


def test_dynamic_tanh_respects_bias_at_zero() -> None:
    assert dynamic_tanh(0.0, alpha=2.0, gamma=3.0, beta=0.5) == pytest.approx(0.5)


def test_scalar_activations_requires_non_negative_alpha() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        scalar_activations(1.0, alpha=-0.1)


def test_softmax_requires_non_empty_row() -> None:
    with pytest.raises(ValueError, match="non-empty"):
        softmax([])
