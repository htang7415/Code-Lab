"""Causal (masked) self-attention from scratch using NumPy."""

import numpy as np


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    """Numerically stable softmax."""
    x_max = np.max(x, axis=axis, keepdims=True)
    e_x = np.exp(x - x_max)
    return e_x / np.sum(e_x, axis=axis, keepdims=True)


def causal_mask(seq_len: int) -> np.ndarray:
    """Return an upper-triangular matrix of -inf (causal mask).

    Shape: (seq_len, seq_len). mask[i][j] = -inf if j > i, else 0.
    """
    mask = np.zeros((seq_len, seq_len))
    mask[np.triu_indices(seq_len, k=1)] = -np.inf
    return mask


def causal_self_attention(
    Q: np.ndarray, K: np.ndarray, V: np.ndarray
) -> np.ndarray:
    """Compute causal self-attention.

    Args:
        Q: queries, shape (seq_len, d_k)
        K: keys,    shape (seq_len, d_k)
        V: values,  shape (seq_len, d_v)

    Returns:
        output of shape (seq_len, d_v)
    """
    seq_len, d_k = Q.shape
    scores = Q @ K.T / np.sqrt(d_k)
    scores = scores + causal_mask(seq_len)
    weights = softmax(scores, axis=-1)
    return weights @ V
