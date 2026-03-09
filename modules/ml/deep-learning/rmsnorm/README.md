# RMSNorm

> Track: `ml` | Topic: `deep-learning`

## Concept

RMSNorm rescales a vector by its root-mean-square magnitude without subtracting
the mean. Compared with LayerNorm, it keeps the direction of the centered signal
less explicit and focuses only on controlling scale.

## Math

$$y = \frac{x}{\sqrt{\frac{1}{d}\sum_{i=1}^{d} x_i^2 + \epsilon}}$$

- $x \in \mathbb{R}^d$ -- input vector
- $x_i$ -- i-th coordinate of the input
- $d$ -- hidden dimension
- $\epsilon$ -- small constant for numerical stability
- $y$ -- normalized output vector

## Key Points

- RMSNorm controls scale but does not center activations.
- If the RMS of $x$ is large, the vector is scaled down; if it is small, the
  vector is scaled up.
- This is why RMSNorm is cheaper than mean-and-variance normalization.

## Function

```python
def rmsnorm(x: list[float], eps: float = 1e-5) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/rmsnorm/python -q
```
