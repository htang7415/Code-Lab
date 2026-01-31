from __future__ import annotations

import math


def _softmax(row: list[float]) -> list[float]:
    m = max(row)
    exps = [math.exp(x - m) for x in row]
    s = sum(exps)
    return [e / s for e in exps]


def next_token_loss(logits: list[list[float]], targets: list[int]) -> float:
    total = 0.0
    for row, tgt in zip(logits, targets):
        probs = _softmax(row)
        total += -math.log(probs[tgt])
    return total / len(targets)
