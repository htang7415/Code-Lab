# Positional Encoding

> Track: `ml` | Topic: `llm`

## Concept

Positional encodings add order information to token embeddings.

## Math

$$
\mathrm{PE}[pos,2i] = \sin\left(\frac{pos}{10000^{2i/d}}\right),\quad
\mathrm{PE}[pos,2i+1] = \cos\left(\frac{pos}{10000^{2i/d}}\right).
$$

- $i$ -- index
- $d$ -- dimension

## Function

```python
def sinusoidal_position(pos: int, d_model: int) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/llm/positional-encoding/python -q
```
