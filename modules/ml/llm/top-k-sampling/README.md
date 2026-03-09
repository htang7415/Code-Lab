# Top-k Sampling Filter

> Track: `ml` | Topic: `llm`

## Concept

Top-k sampling keeps only the $k$ most probable next tokens and discards the rest before sampling.

## Math

$$S = \operatorname{TopK}(p, k)$$

- $p$ -- next-token probability distribution
- $k$ -- number of highest-probability tokens retained
- $S$ -- retained token index set

## Key Points

- Top-k uses a fixed candidate set size.
- Unlike top-p, it does not adapt to distribution shape.
- This module returns the kept token indices, not a random sample.

## Function

```python
def top_k_filter(probabilities: list[float], k: int) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/llm/top-k-sampling/python -q
```
