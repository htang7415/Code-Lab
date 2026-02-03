# Zeroing Gradients

> Track: `ml` | Topic: `systems`

## Concept

Zeroing gradients resets all parameter gradient buffers to zero before the next backward pass. In most deep learning frameworks, gradients are accumulated by default rather than overwritten, so calling the backward pass without zeroing first will add the new gradients on top of the old ones. This is almost always a bug -- unless you are intentionally using gradient accumulation.

The standard training loop follows the pattern: zero gradients, forward pass, compute loss, backward pass, optimizer step. Forgetting the zeroing step is one of the most common mistakes when writing training loops from scratch. The resulting incorrect gradient accumulation causes erratic loss curves and makes the model appear to diverge even when the learning rate and architecture are correct. Frameworks like PyTorch provide `optimizer.zero_grad()` to handle this in one call across all parameter groups.

## Math

Before each backward pass, every gradient buffer is reset:

$$g_i \leftarrow 0, \quad \forall\, i \in \{1, \dots, P\}$$

Without zeroing, the gradient at iteration $t$ incorrectly becomes:

$$g_i^{(t)} = \sum_{s=1}^{t} \nabla_{\theta_i} L^{(s)}$$

- $g_i$ -- gradient buffer for parameter $i$
- $P$ -- total number of learnable parameters
- $\nabla_{\theta_i} L^{(s)}$ -- gradient contribution from iteration $s$
- $\theta_i$ -- i-th model parameter
- $t$ -- iteration index
- $s$ -- iteration index
- $L$ -- loss value

## Key Points

- Forgetting to zero gradients causes gradients from previous iterations to accumulate, leading to incorrect and increasingly large updates.
- In PyTorch, `optimizer.zero_grad()` or `model.zero_grad()` clears all gradient buffers; calling it at the start of each iteration is standard practice.
- When using gradient accumulation intentionally, you skip the zeroing step for $K-1$ micro-batches and only zero after the optimizer step.
- Setting gradients to `None` instead of zero can be slightly more memory-efficient in some frameworks, as it avoids allocating the zero tensor.

## Function

```python
def zero_grad(grads: list[float]) -> list[float]:
```

- `grads` -- list of current gradient values (one per parameter) to be reset to zero

## Run tests

```bash
pytest modules/ml/systems/zero-gradients/python -q
```
