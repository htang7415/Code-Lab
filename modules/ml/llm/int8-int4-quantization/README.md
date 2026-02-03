# INT8/INT4 Quantization

> Track: `ml` | Topic: `llm`

## Concept

Integer quantization maps floats to a small integer range with a scale.

## Math
$$q = \mathrm{round}(x / s),\quad \hat{x} = q \cdot s$$

- $q$ -- quantized integer value
- $x$ -- input value
- $s$ -- quantization scale
- $\hat{x}$ -- dequantized value

## Function

```python
def quantize_int(x: float, bits: int, scale: float) -> int:
```

## Run tests

```bash
pytest modules/ml/llm/int8-int4-quantization/python -q
```