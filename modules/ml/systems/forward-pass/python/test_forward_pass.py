import pytest

from forward_pass import forward


def test_forward():
    assert forward([1.0, 2.0], [1.0, 1.0], 0.0) == 3.0


def test_forward_applies_bias_after_dot_product():
    assert forward([2.0, -1.0], [3.0, 4.0], 0.5) == 2.5


def test_forward_rejects_length_mismatch():
    with pytest.raises(ValueError, match="same length"):
        forward([1.0], [1.0, 2.0], 0.0)
