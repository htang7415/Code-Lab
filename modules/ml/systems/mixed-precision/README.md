# Mixed Precision Training

> Track: `ml` | Topic: `systems`

## Concept

Mixed precision training accelerates deep learning by performing the forward and backward passes in half precision (FP16) while maintaining a master copy of the weights in full precision (FP32). FP16 arithmetic is significantly faster on modern GPUs equipped with tensor cores and uses half the memory, enabling larger models and batch sizes. The FP32 master weights ensure that small gradient updates are not lost due to the limited precision of FP16.

The main challenge with FP16 is its narrow dynamic range: gradients can underflow to zero during the backward pass. Loss scaling addresses this by multiplying the loss by a large factor before backpropagation, which shifts the gradients into the representable FP16 range. After the backward pass, the scaled gradients are divided by the same factor before the optimizer step. An alternative is BF16 (bfloat16), which has the same exponent range as FP32 and therefore rarely requires loss scaling, though it sacrifices some mantissa precision.

## Math

The loss-scaled backward pass computes:

$$g_{\text{scaled}} = \frac{\partial (S \cdot L)}{\partial \theta} = S \cdot \frac{\partial L}{\partial \theta}$$

Before the optimizer update, the gradients are unscaled:

$$g = \frac{g_{\text{scaled}}}{S}$$

The master weight update remains in FP32:

$$\theta_{\text{FP32}} \leftarrow \theta_{\text{FP32}} - \alpha \cdot g$$

- $S$ -- loss scale factor (a large constant, often dynamically adjusted)
- $L$ -- loss value
- $g$ -- true gradient in FP32
- $g_{\text{scaled}}$ -- gradient computed under loss scaling in FP16
- $\alpha$ -- learning rate
- $\theta_{\text{FP32}}$ -- master copy of weights in full precision

## Key Points

- Loss scaling prevents gradient underflow in FP16 by shifting small gradient magnitudes into the representable range.
- BF16 has the same exponent range as FP32, so it largely eliminates the need for loss scaling at the cost of slightly lower mantissa precision.
- Always keep the optimizer state and master weights in FP32 -- accumulating small updates in FP16 leads to stagnation.
- Dynamic loss scaling automatically adjusts the scale factor: it increases the scale when no overflow is detected and decreases it upon encountering Inf or NaN gradients.

## Function

```python
def scale_gradients(grads: list[float], scale: float) -> list[float]:
```

- `grads` -- list of gradient values to be scaled
- `scale` -- loss scale factor $S$ to multiply each gradient by

## Run tests

```bash
pytest modules/ml/systems/mixed-precision/python -q
```
