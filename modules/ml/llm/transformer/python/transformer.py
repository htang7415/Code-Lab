from __future__ import annotations

import math


def _softmax(row: list[float]) -> list[float]:
    m = max(row)
    exps = [math.exp(x - m) for x in row]
    s = sum(exps)
    return [e / s for e in exps]


def _matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    out = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            row.append(sum(a[i][k] * b[k][j] for k in range(len(b))))
        out.append(row)
    return out


def _transpose(a: list[list[float]]) -> list[list[float]]:
    return [list(col) for col in zip(*a)]


def _self_attention(x: list[list[float]]) -> list[list[float]]:
    dk = len(x[0])
    scores = _matmul(x, _transpose(x))
    scaled = [[val / math.sqrt(dk) for val in row] for row in scores]
    weights = [_softmax(row) for row in scaled]
    return _matmul(weights, x)


def _relu_row(row: list[float]) -> list[float]:
    return [max(0.0, x) for x in row]


def transformer_block(x: list[list[float]], w1: list[list[float]], w2: list[list[float]]) -> list[list[float]]:
    attn = _self_attention(x)
    res1 = [[x[i][j] + attn[i][j] for j in range(len(x[0]))] for i in range(len(x))]
    ffn_hidden = _matmul(res1, w1)
    ffn_hidden = [_relu_row(row) for row in ffn_hidden]
    ffn = _matmul(ffn_hidden, w2)
    res2 = [[res1[i][j] + ffn[i][j] for j in range(len(ffn[0]))] for i in range(len(ffn))]
    return res2
