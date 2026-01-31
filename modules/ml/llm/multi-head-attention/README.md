# Multi-Head Attention

> Track: `ml` | Topic: `llm`

## Concept

Multi-head attention runs attention in parallel subspaces and concatenates results.

## Math

$$Split Q,K,V into heads: head_i = Attention(Q_i,K_i,V_i).$$

## Function

```python
def multi_head_attention(q: list[list[float]], k: list[list[float]], v: list[list[float]], heads: int) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/multi-head-attention/python -q
```
