# Top-p Sampling Filter

> Track: `ml` | Topic: `llm`

## Concept

Top-p sampling keeps the smallest set of high-probability tokens whose cumulative probability reaches a target threshold $p$.

## Math

$$S = \min \left\{ k : \sum_{i=1}^{k} p_{(i)} \ge p \right\}$$

- $p_{(i)}$ -- token probabilities sorted from largest to smallest
- $S$ -- cutoff rank after sorting
- $p$ -- nucleus threshold

## Key Points

- Top-p adapts the candidate set size to the shape of the distribution.
- Peaked distributions keep very few tokens; flatter ones keep more.
- This module returns the kept token indices, not a random sample.

## Function

```python
def top_p_filter(probabilities: list[float], p: float) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/llm/top-p-sampling/python -q
```
