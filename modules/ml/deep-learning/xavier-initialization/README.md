# Xavier/Glorot Initialization

> Track: `ml` | Topic: `deep-learning`

## Concept

Xavier init keeps variance stable for symmetric activations.

## Math

$$W \sim \mathcal{U}\left(-\sqrt{\frac{6}{fan_{in}+fan_{out}}}, \sqrt{\frac{6}{fan_{in}+fan_{out}}}\right)$$

## Function

```python
def xavier_uniform(fan_in: int, fan_out: int, seed: int = 0) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/xavier-initialization/python -q
```
