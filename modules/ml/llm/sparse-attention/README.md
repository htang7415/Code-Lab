# Sparse Attention

> Track: `ml` | Topic: `llm`

## Concept

Sparse attention limits attention to a local window to reduce complexity.

## Math

$$Mask scores outside a window so softmax only sees nearby positions.$$

## Function

```python
def window_mask(seq_len: int, window: int) -> list[list[int]]:
```

## Run tests

```bash
pytest modules/ml/llm/sparse-attention/python -q
```
