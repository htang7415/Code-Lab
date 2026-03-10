import pytest

from global_average_pooling import global_average_pool


def test_global_average_pool_returns_feature_map_mean() -> None:
    pooled = global_average_pool([[1.0, 3.0], [5.0, 7.0]])

    assert pooled == pytest.approx(4.0)


def test_global_average_pool_supports_rectangular_maps() -> None:
    pooled = global_average_pool([[2.0, 4.0, 6.0]])

    assert pooled == pytest.approx(4.0)


def test_global_average_pool_requires_consistent_row_widths() -> None:
    with pytest.raises(ValueError, match="equal length"):
        global_average_pool([[1.0, 2.0], [3.0]])
