# Multi-Head Attention

> Track: `ml` | Topic: `llm`

## Concept

Multi-head attention runs attention in parallel subspaces and concatenates results.

## Math
$$\mathrm{head}_i = \mathrm{Attention}(Q_i, K_i, V_i),\quad \mathrm{MHA}(Q,K,V) = \mathrm{Concat}(\mathrm{head}_i) W^O$$

- $W^O$ -- output projection matrix
- $Q_i$ -- i-th query matrix
- $K_i$ -- i-th key matrix
- $V_i$ -- i-th value matrix
- $i$ -- index
- $Q$ -- query matrix
- $K$ -- key matrix
- $V$ -- value matrix
- $W$ -- weight matrix

## Function

```python
def multi_head_attention(q: list[list[float]], k: list[list[float]], v: list[list[float]], heads: int) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/multi-head-attention/python -q
```