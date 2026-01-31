from __future__ import annotations

import math


def _softmax(row: list[float]) -> list[float]:
    m = max(row)
    exps = [math.exp(x - m) for x in row]
    s = sum(exps)
    return [e / s for e in exps]


def sft_loss(logits: list[list[float]], targets: list[int], mask: list[int]) -> float:
    total = 0.0
    count = 0
    for row, tgt, keep in zip(logits, targets, mask):
        if not keep:
            continue
        probs = _softmax(row)
        total += -math.log(probs[tgt])
        count += 1
    return total / max(count, 1)
