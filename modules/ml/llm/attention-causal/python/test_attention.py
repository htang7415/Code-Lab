import numpy as np
from attention import causal_mask, causal_self_attention, softmax


def test_softmax_sums_to_one():
    x = np.array([[1.0, 2.0, 3.0]])
    s = softmax(x)
    np.testing.assert_allclose(s.sum(axis=-1), 1.0, atol=1e-6)


def test_causal_mask_shape():
    mask = causal_mask(4)
    assert mask.shape == (4, 4)


def test_causal_mask_lower_triangular():
    mask = causal_mask(3)
    # Lower-triangular part (including diagonal) should be 0
    assert mask[0, 0] == 0.0
    assert mask[1, 0] == 0.0
    assert mask[1, 1] == 0.0
    assert mask[2, 2] == 0.0
    # Upper-triangular part should be -inf
    assert mask[0, 1] == -np.inf
    assert mask[0, 2] == -np.inf
    assert mask[1, 2] == -np.inf


def test_causal_attention_output_shape():
    seq_len, d_k, d_v = 5, 8, 4
    rng = np.random.default_rng(42)
    Q = rng.standard_normal((seq_len, d_k))
    K = rng.standard_normal((seq_len, d_k))
    V = rng.standard_normal((seq_len, d_v))
    out = causal_self_attention(Q, K, V)
    assert out.shape == (seq_len, d_v)


def test_causal_attention_no_future_leakage():
    """The first token's output must depend only on the first row of V."""
    seq_len, d = 4, 2
    Q = np.ones((seq_len, d))
    K = np.ones((seq_len, d))
    V = np.eye(seq_len, d)  # each row is distinct
    out = causal_self_attention(Q, K, V)
    # First token can only attend to itself, so output[0] == V[0]
    np.testing.assert_allclose(out[0], V[0], atol=1e-6)
