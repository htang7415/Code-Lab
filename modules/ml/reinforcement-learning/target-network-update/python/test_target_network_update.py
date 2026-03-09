import pytest

from target_network_update import soft_target_update


def test_soft_target_update_interpolates_between_target_and_online_values() -> None:
    updated = soft_target_update(target_values=[1.0, 2.0], online_values=[3.0, 4.0], tau=0.25)

    assert updated == pytest.approx([1.5, 2.5])


def test_soft_target_update_with_zero_tau_keeps_target_values() -> None:
    updated = soft_target_update(target_values=[1.0], online_values=[10.0], tau=0.0)

    assert updated == pytest.approx([1.0])


def test_soft_target_update_requires_valid_tau() -> None:
    with pytest.raises(ValueError, match="tau"):
        soft_target_update(target_values=[1.0], online_values=[2.0], tau=1.5)
