import math

import pytest

from bic_aic import aic_bic


def test_aic_bic_matches_closed_form() -> None:
    aic, bic = aic_bic(log_likelihood=-120.5, num_params=4, num_samples=100)

    assert aic == pytest.approx(249.0)
    assert bic == pytest.approx(259.4206807439524)


def test_aic_bic_allows_zero_parameters() -> None:
    aic, bic = aic_bic(log_likelihood=-2.0, num_params=0, num_samples=10)

    assert aic == 4.0
    assert bic == 4.0


def test_aic_bic_requires_positive_sample_count() -> None:
    with pytest.raises(ValueError, match="positive"):
        aic_bic(log_likelihood=0.0, num_params=1, num_samples=0)
