import pytest

from ema_diffusion_weights import ema_update


def test_ema_update_blends_old_and_new_weights() -> None:
    updated = ema_update([1.0, 2.0], [3.0, 0.0], decay=0.9)

    assert updated == pytest.approx([1.2, 1.8])


def test_ema_update_with_zero_decay_copies_live_weights() -> None:
    updated = ema_update([1.0, 2.0], [3.0, 0.0], decay=0.0)

    assert updated == pytest.approx([3.0, 0.0])


def test_ema_update_requires_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        ema_update([1.0], [1.0, 2.0], decay=0.9)
