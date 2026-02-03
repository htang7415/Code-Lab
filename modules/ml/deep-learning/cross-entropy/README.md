# Cross-Entropy Loss

> Track: `ml` | Topic: `deep-learning`

## Concept

Cross-entropy compares a predicted distribution to a target class.

## Math

$$L = -\log\left(\mathrm{softmax}(\text{logits})_{\text{target}}\right)$$

- $L$ -- loss value

## Function

```python
def cross_entropy(logits: list[float], target: int) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/cross-entropy/python -q
```
