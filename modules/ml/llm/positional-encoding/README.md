# Positional Encoding

> Track: `ml` | Topic: `llm`

## Concept

Positional encodings add order information to token embeddings.

## Math

Sinusoidal: `PE[pos,2i]=sin(pos/10000^{2i/d})`, `PE[pos,2i+1]=cos(pos/10000^{2i/d})`.

## Function

```python
def sinusoidal_position(pos: int, d_model: int) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/llm/positional-encoding/python -q
```
