import pytest

from lle import lle_weights


def test_lle_weights_are_balanced_for_orthogonal_neighbors() -> None:
    weights = lle_weights(
        point=[0.0, 0.0],
        neighbors=[[1.0, 0.0], [0.0, 1.0]],
    )

    assert weights[0] == pytest.approx(0.5)
    assert weights[1] == pytest.approx(0.5)


def test_lle_weights_return_one_for_single_neighbor() -> None:
    assert lle_weights(point=[1.0], neighbors=[[0.0]]) == [1.0]


def test_lle_weights_require_matching_dimensions() -> None:
    with pytest.raises(ValueError, match="dimension"):
        lle_weights(point=[0.0, 0.0], neighbors=[[1.0]])
