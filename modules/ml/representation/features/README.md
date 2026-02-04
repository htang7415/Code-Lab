# Feature Vectors

> Track: `ml` | Topic: `representation`

## Concept

Feature vectors convert variable-length inputs into a fixed-size numeric form
that models can consume.

## Math

For a vocabulary of size $V$:

$$x_i = \text{count}(\text{token}_i)$$

## Function

```python
def bag_of_words(tokens: list[str], vocab: list[str]) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/representation/features/python -q
```
