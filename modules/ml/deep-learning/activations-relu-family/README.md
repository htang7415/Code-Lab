# ReLU Family

> Track: `ml` | Topic: `deep-learning`

## Concept

ReLU variants improve gradient flow by keeping nonzero slopes.

## Math

$$\mathrm{ReLU}(x)=\max(0,x),\ \mathrm{LeakyReLU}(x)=\max(\alpha x,x)$$

## Function

```python
def relu_family(x: float, alpha: float = 0.01) -> dict[str, float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/activations-relu-family/python -q
```
