"""Muon optimizer demo using Gram-Schmidt orthogonalization."""

from __future__ import annotations

import math
from typing import List, Tuple


Matrix = List[List[float]]


def _dot(a: List[float], b: List[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def _norm(v: List[float]) -> float:
    return math.sqrt(_dot(v, v))


def gram_schmidt_rows(mat: Matrix, eps: float = 1e-12) -> Matrix:
    """Return an orthonormalized copy of rows via Gram-Schmidt."""
    out: Matrix = []
    for row in mat:
        v = row[:]
        for u in out:
            proj = _dot(v, u)
            v = [vi - proj * ui for vi, ui in zip(v, u)]
        n = _norm(v)
        if n < eps:
            out.append([0.0 for _ in v])
        else:
            out.append([vi / n for vi in v])
    return out


def muon_step(
    weights: Matrix,
    grad: Matrix,
    velocity: Matrix | None,
    lr: float = 0.1,
    momentum: float = 0.9,
) -> Tuple[Matrix, Matrix]:
    """Apply a Muon-style update and return (new_weights, new_velocity)."""
    if velocity is None:
        velocity = [[0.0 for _ in row] for row in grad]
    new_velocity = [
        [momentum * v + g for v, g in zip(v_row, g_row)]
        for v_row, g_row in zip(velocity, grad)
    ]
    ortho = gram_schmidt_rows(new_velocity)
    new_weights = [
        [w - lr * u for w, u in zip(w_row, u_row)]
        for w_row, u_row in zip(weights, ortho)
    ]
    return new_weights, new_velocity
