# Self-Attention

> Track: `ml` | Topic: `llm`

## Concept

Self-attention lets each token attend to all others by comparing queries and keys.

## Math

Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) V

## Function

```python
def self_attention(q: list[list[float]], k: list[list[float]], v: list[list[float]]) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/self-attention/python -q
```
