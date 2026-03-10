import pytest

from qk_clip import qk_clip


def test_qk_clip_limits_scores_to_threshold() -> None:
    clipped = qk_clip([[0.5, -2.0], [3.0, -0.25]], clip_value=1.0)

    assert clipped == [[0.5, -1.0], [1.0, -0.25]]


def test_qk_clip_leaves_small_scores_unchanged() -> None:
    clipped = qk_clip([[0.1, -0.2], [0.3]], clip_value=2.0)

    assert clipped == [[0.1, -0.2], [0.3]]


def test_qk_clip_requires_positive_threshold() -> None:
    with pytest.raises(ValueError, match="positive"):
        qk_clip([[1.0]], clip_value=0.0)
