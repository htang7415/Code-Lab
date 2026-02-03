# FP16/BF16/FP8 Precision

> Track: `ml` | Topic: `llm`

## Concept

Lower-precision formats trade accuracy for speed and memory.

## Math
$$x_q = \mathrm{round}(x / s) \cdot s$$

- $x$ -- input value
- $x_q$ -- quantized value
- $s$ -- quantization scale

## Function

```python
def quantize_fp(x: float, mantissa_bits: int) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/fp16-bf16-fp8/python -q
```