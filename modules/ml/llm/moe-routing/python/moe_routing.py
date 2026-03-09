"""Sparse Mixture-of-Experts layer using top-k routing."""

from __future__ import annotations

import numpy as np


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    """Compute a numerically stable softmax."""
    x_max = np.max(x, axis=axis, keepdims=True)
    exp_x = np.exp(x - x_max)
    return exp_x / np.sum(exp_x, axis=axis, keepdims=True)


def moe(
    x: np.ndarray,
    We: np.ndarray,
    Wg: np.ndarray,
    n_experts: int,
    top_k: int,
) -> np.ndarray:
    """Apply a sparse Mixture-of-Experts layer.

    Args:
        x: Input tensor of shape (n_batch, l_seq, d_model).
        We: Expert weights of shape (n_experts, d_model, d_model).
        Wg: Gating weights of shape (d_model, n_experts).
        n_experts: Number of experts.
        top_k: Number of experts to route each token to.

    Returns:
        Output tensor of shape (n_batch, l_seq, d_model).
    """
    if x.ndim != 3:
        raise ValueError("x must have shape (n_batch, l_seq, d_model)")
    if We.ndim != 3:
        raise ValueError("We must have shape (n_experts, d_model, d_model)")
    if Wg.ndim != 2:
        raise ValueError("Wg must have shape (d_model, n_experts)")
    if top_k < 1 or top_k > n_experts:
        raise ValueError("top_k must satisfy 1 <= top_k <= n_experts")

    n_batch, l_seq, d_model = x.shape
    if We.shape != (n_experts, d_model, d_model):
        raise ValueError("We shape must be (n_experts, d_model, d_model)")
    if Wg.shape != (d_model, n_experts):
        raise ValueError("Wg shape must be (d_model, n_experts)")

    compute_dtype = np.result_type(x.dtype, We.dtype, Wg.dtype, np.float32)
    x_flat = x.reshape(-1, d_model).astype(compute_dtype, copy=False)
    We = We.astype(compute_dtype, copy=False)
    Wg = Wg.astype(compute_dtype, copy=False)
    n_tokens = x_flat.shape[0]

    logits = x_flat @ Wg
    probs = softmax(logits, axis=-1)

    topk_idx = np.argpartition(-probs, kth=top_k - 1, axis=-1)[:, :top_k]
    topk_probs = np.take_along_axis(probs, topk_idx, axis=-1)

    order = np.argsort(-topk_probs, axis=-1)
    topk_idx = np.take_along_axis(topk_idx, order, axis=-1)
    topk_probs = np.take_along_axis(topk_probs, order, axis=-1)
    topk_probs = topk_probs / np.sum(topk_probs, axis=-1, keepdims=True)

    out = np.zeros((n_tokens, d_model), dtype=compute_dtype)
    for slot in range(top_k):
        expert_ids = topk_idx[:, slot]
        expert_weights = topk_probs[:, slot]
        transformed = np.einsum("td,tdh->th", x_flat, We[expert_ids])
        out += expert_weights[:, None] * transformed

    return out.reshape(n_batch, l_seq, d_model)
