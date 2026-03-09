from __future__ import annotations

import pytest

from breach_spectrum import breach_spectrum


def test_breach_spectrum_counts_breaches_by_severity_bucket() -> None:
    counts = breach_spectrum([0.9, 1.05, 1.2, 1.5], capacity=1.0, cutoffs=[0.1, 0.3])

    assert counts == [1, 1, 1]


def test_breach_spectrum_returns_zero_counts_when_there_are_no_breaches() -> None:
    assert breach_spectrum([0.5, 0.8], capacity=1.0, cutoffs=[0.1, 0.3]) == [0, 0, 0]


def test_breach_spectrum_rejects_unsorted_cutoffs() -> None:
    with pytest.raises(ValueError, match="sorted"):
        breach_spectrum([1.2], capacity=1.0, cutoffs=[0.3, 0.1])
