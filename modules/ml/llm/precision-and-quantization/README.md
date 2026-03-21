# Precision and Quantization

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to compare the main numeric-format choices in LLM training and inference: lower-precision floating point and integer quantization.

## First Principles

- Lower precision reduces memory traffic and usually improves throughput.
- FP16, BF16, and FP8 keep floating-point behavior with fewer bits.
- INT8 and INT4 use explicit scale factors and integer storage.
- These choices trade off memory, speed, dynamic range, and numerical stability.

## Core Math

Floating-point rounding view:

$$
x_q \approx \mathrm{round}(x / s)\cdot s
$$

Integer quantization:

$$
q = \mathrm{round}(x / s), \quad \hat{x} = q \cdot s
$$

## Minimal Code Mental Model

```python
fp_value = quantize_fp(x=1.2345, mantissa_bits=3)
int_value = quantize_int(x=1.2, bits=4, scale=0.1)
```

## Function

```python
def quantize_fp(x: float, mantissa_bits: int) -> float:
def quantize_int(x: float, bits: int, scale: float) -> int:
```

## When To Use What

- Use lower-precision floating point when you want training or inference speedups with less disruption than integer quantization.
- Use INT8 or INT4 when memory savings are the main goal and some quantization error is acceptable.

## References

- Micikevicius et al. (2018). [Mixed Precision Training](https://arxiv.org/abs/1710.03740)
- Micikevicius et al. (2022). [FP8 Formats for Deep Learning](https://arxiv.org/abs/2209.05433)
- Dettmers et al. (2022). [LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale](https://arxiv.org/abs/2208.07339)
- Frantar et al. (2022). [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://arxiv.org/abs/2210.17323)

## Run tests

```bash
pytest modules/ml/llm/precision-and-quantization/python -q
```
