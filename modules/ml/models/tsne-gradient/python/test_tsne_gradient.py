import pytest

from tsne_gradient import tsne_point_gradient


def test_tsne_point_gradient_is_zero_for_symmetric_match() -> None:
    gradient = tsne_point_gradient(
        point=[0.0, 0.0],
        other_points=[[1.0, 0.0], [-1.0, 0.0]],
        affinities=[0.5, 0.5],
    )

    assert gradient == pytest.approx([0.0, 0.0])


def test_tsne_point_gradient_moves_toward_higher_affinity_neighbor() -> None:
    gradient = tsne_point_gradient(
        point=[0.0, 0.0],
        other_points=[[1.0, 0.0], [-1.0, 0.0]],
        affinities=[0.8, 0.2],
    )

    assert gradient == pytest.approx([-1.2, 0.0])


def test_tsne_point_gradient_requires_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        tsne_point_gradient([0.0], [[1.0]], [0.5, 0.5])
