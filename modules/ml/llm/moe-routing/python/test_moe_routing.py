import numpy as np
import pytest

from moe_routing import moe


def test_moe_output_shape():
    rng = np.random.default_rng(42)
    x = rng.standard_normal((2, 3, 4))
    We = rng.standard_normal((3, 4, 4))
    Wg = rng.standard_normal((4, 3))

    out = moe(x, We, Wg, n_experts=3, top_k=2)

    assert out.shape == (2, 3, 4)


def test_moe_top1_routes_to_single_expert():
    x = np.array([[[1.0, 2.0], [-1.0, -2.0]]])
    We = np.array(
        [
            [[1.0, 0.0], [0.0, 1.0]],
            [[2.0, 0.0], [0.0, 2.0]],
        ]
    )
    Wg = np.array([[1.0, -1.0], [1.0, -1.0]])

    out = moe(x, We, Wg, n_experts=2, top_k=1)

    expected = np.array([[[1.0, 2.0], [-2.0, -4.0]]])
    np.testing.assert_allclose(out, expected, atol=1e-6)


def test_moe_topk_probabilities_are_renormalized():
    x = np.array([[[1.0]]])
    We = np.array([[[1.0]], [[2.0]], [[4.0]]])
    Wg = np.array([[0.0, 1.0, 2.0]])

    out = moe(x, We, Wg, n_experts=3, top_k=2)

    probs = np.exp([0.0, 1.0, 2.0])
    probs = probs / probs.sum()
    top2 = probs[1:]
    top2 = top2 / top2.sum()
    expected = top2[0] * 2.0 + top2[1] * 4.0
    np.testing.assert_allclose(out, np.array([[[expected]]]), atol=1e-6)


def test_moe_rejects_invalid_topk():
    x = np.ones((1, 1, 2))
    We = np.ones((2, 2, 2))
    Wg = np.ones((2, 2))

    with pytest.raises(ValueError, match="top_k"):
        moe(x, We, Wg, n_experts=2, top_k=3)
