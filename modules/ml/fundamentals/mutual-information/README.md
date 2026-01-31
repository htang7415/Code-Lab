# Mutual Information

> Track: `ml` | Topic: `fundamentals`

## Concept

Mutual information measures shared information between variables.

## Math

$$I(X;Y)=\sum_{x,y} p(x,y)\log\left(\frac{p(x,y)}{p(x)p(y)}\right)$$

## Function

```python
def mutual_information(joint: list[list[float]]) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/mutual-information/python -q
```
