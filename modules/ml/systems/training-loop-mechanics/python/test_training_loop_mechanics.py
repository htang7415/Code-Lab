from __future__ import annotations

import pytest

from training_loop_mechanics import (
    accumulate,
    backward,
    forward,
    gradients_ok,
    scale_gradients,
    step,
    zero_grad,
)


def test_zero_grad_resets_values() -> None:
    assert zero_grad([1.0, -1.0]) == [0.0, 0.0]


def test_forward_computes_affine_output() -> None:
    assert forward([1.0, 2.0], [1.0, 1.0], 0.0) == 3.0
    assert forward([2.0, -1.0], [3.0, 4.0], 0.5) == 2.5


def test_forward_rejects_length_mismatch() -> None:
    with pytest.raises(ValueError, match="same length"):
        forward([1.0], [1.0, 2.0], 0.0)


def test_backward_returns_local_gradient() -> None:
    assert backward(2.0, 3.0) == 6.0


def test_step_applies_gradient_update() -> None:
    assert step(1.0, 0.5, 0.1) == 0.95


def test_accumulate_sums_micro_batch_gradients() -> None:
    assert accumulate([[1.0, 2.0], [3.0, 4.0]]) == [4.0, 6.0]


def test_scale_gradients_multiplies_by_scale() -> None:
    assert scale_gradients([1.0, 2.0], 2.0) == [2.0, 4.0]


def test_gradients_ok_checks_for_signal() -> None:
    assert gradients_ok([0.0, 1.0])
    assert not gradients_ok([0.0, 0.0])
