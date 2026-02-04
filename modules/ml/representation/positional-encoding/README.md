# Positional Encoding

> Track: `ml` | Topic: `representation`

## Concept

Positional encodings inject order information so models can distinguish
token positions in a sequence.

## Math

For position $p$ and dimension $i$:

$$
\text{PE}(p, 2i) = \sin\left(\frac{p}{10000^{2i/d}}\right), \quad
\text{PE}(p, 2i+1) = \cos\left(\frac{p}{10000^{2i/d}}\right)
$$

## Function

```python
def sinusoidal_position_encoding(length: int, dim: int) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/representation/positional-encoding/python -q
```
