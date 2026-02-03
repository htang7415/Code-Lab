# Dropout

> Track: `ml` | Topic: `deep-learning`

## Concept

Dropout randomly zeroes activations during training to reduce co-adaptation.

## Math
$$x' = \frac{m \odot x}{1-p},\quad m \sim \mathrm{Bernoulli}(1-p)$$

- $x$ -- input (feature vector or sample)
- $p$ -- probability
- $m$ -- number of features/units

## Function

```python
def dropout(x: list[float], p: float, seed: int = 0) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/dropout/python -q
```