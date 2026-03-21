import pytest

from rope_and_position_scaling import (
    linear_scaled_position,
    rope_pair_frequency,
    rope_rotation_angle,
    rope_scaled_angle,
)


def test_rope_pair_frequency_matches_known_small_example() -> None:
    assert rope_pair_frequency(pair_index=0, d_model=8) == pytest.approx(1.0)
    assert rope_pair_frequency(pair_index=1, d_model=8) == pytest.approx(0.1)


def test_rope_rotation_angle_multiplies_position_by_frequency() -> None:
    freq = rope_pair_frequency(pair_index=1, d_model=8)
    assert rope_rotation_angle(position=50.0, pair_index=1, d_model=8) == pytest.approx(
        50.0 * freq
    )


def test_linear_scaled_position_maps_target_window_back_to_training_window() -> None:
    assert linear_scaled_position(position=8192, original_context=4096, target_context=8192) == pytest.approx(
        4096.0
    )


def test_rope_scaled_angle_uses_scaled_position_before_rotation() -> None:
    scaled = linear_scaled_position(position=8192, original_context=4096, target_context=8192)
    assert rope_scaled_angle(
        position=8192,
        pair_index=1,
        d_model=8,
        original_context=4096,
        target_context=8192,
    ) == pytest.approx(rope_rotation_angle(position=scaled, pair_index=1, d_model=8))


def test_rope_validates_inputs() -> None:
    with pytest.raises(ValueError, match="even"):
        rope_pair_frequency(pair_index=0, d_model=7)
    with pytest.raises(ValueError, match="feature pairs"):
        rope_pair_frequency(pair_index=4, d_model=8)
    with pytest.raises(ValueError, match="non-negative"):
        rope_rotation_angle(position=-1, pair_index=0, d_model=8)
    with pytest.raises(ValueError, match="at least"):
        linear_scaled_position(position=10, original_context=8192, target_context=4096)
