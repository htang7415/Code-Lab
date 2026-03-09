from __future__ import annotations

import pytest

from breach_bucket_mass import breach_bucket_mass


def test_breach_bucket_mass_normalizes_overload_mass_by_bucket() -> None:
    mass = breach_bucket_mass([0.9, 1.05, 1.2, 1.5], capacity=1.0, cutoffs=[0.1, 0.3])

    assert mass == pytest.approx([0.05 / 0.75, 0.2 / 0.75, 0.5 / 0.75])


def test_breach_bucket_mass_returns_zeros_when_there_is_no_overload() -> None:
    assert breach_bucket_mass([0.5, 0.8], capacity=1.0, cutoffs=[0.1, 0.3]) == [0.0, 0.0, 0.0]


def test_breach_bucket_mass_rejects_unsorted_cutoffs() -> None:
    with pytest.raises(ValueError, match="sorted"):
        breach_bucket_mass([1.2], capacity=1.0, cutoffs=[0.3, 0.1])
