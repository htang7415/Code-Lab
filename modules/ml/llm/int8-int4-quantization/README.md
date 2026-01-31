# INT8/INT4 Quantization

> Track: `ml` | Topic: `llm`

## Concept

Integer quantization maps floats to a small integer range with a scale.

## Math

Quantize: q = round(x / s), dequantize: x̂ = q * s.

## Function

```python
def quantize_int(x: float, bits: int, scale: float) -> int:
```

## Run tests

```bash
pytest modules/ml/llm/int8-int4-quantization/python -q
```
