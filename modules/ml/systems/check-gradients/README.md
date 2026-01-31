# Check Gradients Are Flowing

> Track: `ml` | Topic: `systems`

## Concept

Gradient checking validates that the analytic gradients computed by backpropagation are correct by comparing them against a numerical finite-difference approximation. This is one of the most reliable debugging tools when implementing custom layers, loss functions, or activation functions. If the analytic gradient disagrees with the numerical estimate, there is almost certainly a bug in the backward pass implementation.

The central idea is to perturb each parameter by a small amount $\epsilon$ in both directions and observe how the loss changes. The two-sided finite difference gives a second-order accurate approximation of the true gradient. By computing the relative error between this approximation and the analytic gradient, you can determine whether your implementation is correct. A relative error below $10^{-7}$ typically indicates a correct implementation, while values above $10^{-5}$ suggest a bug.

## Math

The two-sided finite-difference approximation for each parameter $\theta_i$ is:

$$g_{\text{approx},i} = \frac{f(\theta_i + \epsilon) - f(\theta_i - \epsilon)}{2\epsilon}$$

The relative error between the analytic gradient $g$ and the approximation $g_{\text{approx}}$ is:

$$e = \frac{\|g - g_{\text{approx}}\|}{\|g\| + \|g_{\text{approx}}\| + \delta}$$

- $\epsilon$ -- small perturbation, typically $10^{-5}$ to $10^{-7}$
- $g$ -- analytic gradient from backpropagation
- $g_{\text{approx}}$ -- numerical finite-difference gradient
- $\delta$ -- small constant to avoid division by zero

## Key Points

- Use gradient checking only for debugging, never during training -- it is orders of magnitude slower than backpropagation.
- Disable dropout and batch normalization during the check, as their stochastic behavior breaks the finite-difference assumption.
- A relative error below $10^{-7}$ is excellent; between $10^{-5}$ and $10^{-7}$ is acceptable; above $10^{-5}$ likely indicates a bug.
- Check that gradients are non-zero and finite: all-zero gradients signal dead neurons or disconnected graph paths, while NaN or Inf gradients indicate numerical instability.

## Function

```python
def gradients_ok(grads: list[float]) -> bool:
```

- `grads` -- list of gradient values to validate (one per parameter)

## Run tests

```bash
pytest modules/ml/systems/check-gradients/python -q
```
