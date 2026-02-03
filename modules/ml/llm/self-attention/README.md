# Self-Attention

> Track: `ml` | Topic: `llm`

## Concept

Self-attention lets each token attend to all others by comparing queries and keys.

## Math

$$\mathrm{Attention}(Q,K,V) = \mathrm{softmax}\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V$$

- $d_k$ -- key dimension
- $Q$ -- query matrix
- $K$ -- key matrix
- $V$ -- value matrix

- $d$ -- dimension
- $k$ -- index or number of neighbors

## Function

```python
def self_attention(q: list[list[float]], k: list[list[float]], v: list[list[float]]) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/self-attention/python -q
```
