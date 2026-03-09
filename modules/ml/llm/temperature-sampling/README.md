# Temperature Sampling Probabilities

> Track: `ml` | Topic: `llm`

## Concept

Temperature rescales logits before softmax to make generation sharper or flatter.

## Math

$$p_i = \frac{\exp(z_i / T)}{\sum_j \exp(z_j / T)}$$

- $z_i$ -- logit of token $i$
- $T$ -- temperature
- $p_i$ -- rescaled sampling probability

## Key Points

- Lower temperature concentrates probability mass on top tokens.
- Higher temperature spreads mass more evenly.
- Temperature changes randomness without changing the model weights.

## Function

```python
def temperature_probabilities(logits: list[float], temperature: float) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/llm/temperature-sampling/python -q
```
