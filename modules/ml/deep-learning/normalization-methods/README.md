# Normalization Methods

> Track: `ml` | Topic: `deep-learning`

## Concept

Normalization layers stabilize activation scale, but they normalize across
different axes. BatchNorm uses batch statistics, LayerNorm and RMSNorm use
per-token or per-example statistics, and GroupNorm / InstanceNorm sit between
those extremes for vision-style tensors.

## Math

- $\mathrm{BatchNorm}(x)=\frac{x-\mu_B}{\sqrt{\sigma_B^2+\epsilon}}$
- $\mathrm{LayerNorm}(x)=\frac{x-\mu_f}{\sqrt{\sigma_f^2+\epsilon}}$
- $\mathrm{RMSNorm}(x)=\frac{x}{\sqrt{\frac{1}{d}\sum_i x_i^2+\epsilon}}$
- $\mathrm{GroupNorm}(x)=\frac{x-\mu_g}{\sqrt{\sigma_g^2+\epsilon}}$
- $\mathrm{InstanceNorm}(x)=\frac{x-\mu_I}{\sqrt{\sigma_I^2+\epsilon}}$

- $\mu_B$ -- mean over a batch
- $\mu_f$ -- mean over features of one sample
- $\mu_g$ -- mean over one channel group
- $\mu_I$ -- mean over one instance
- $\epsilon$ -- numerical-stability constant

## Key Points

- BatchNorm works well with stable, reasonably large batches, especially in CNNs.
- LayerNorm and RMSNorm avoid cross-example coupling, which is why they fit transformers.
- RMSNorm rescales without subtracting the mean, so it is cheaper than LayerNorm.
- GroupNorm and InstanceNorm are useful when batch statistics are noisy or unavailable.
- BatchNorm is usually a poor fit for transformers because sequence length and batch composition change shared statistics.

## Function

```python
def batchnorm(x: list[float], eps: float = 1e-5) -> list[float]:
def layernorm(x: list[float], eps: float = 1e-5) -> list[float]:
def rmsnorm(x: list[float], eps: float = 1e-5) -> list[float]:
def groupnorm(x: list[float], groups: int, eps: float = 1e-5) -> list[float]:
def instancenorm(x: list[float], eps: float = 1e-5) -> list[float]:
def batch_stats(matrix: list[list[float]]) -> tuple[float, float]:
```

## Pitfalls

- BatchNorm behavior differs between train and eval because running statistics matter in real models.
- Small or variable batch sizes make BatchNorm noisy.
- GroupNorm requires the channel count to be divisible by the number of groups.
- RMSNorm controls scale, not centering, so it is not interchangeable with LayerNorm in every derivation.

## Run tests

```bash
pytest modules/ml/deep-learning/normalization-methods/python -q
```
