# Optimizer Step

> Track: `ml` | Topic: `systems`

## Concept

The optimizer step applies the accumulated gradients to update model parameters, moving them in the direction that reduces the loss. In its simplest form (SGD), each parameter is adjusted by subtracting the gradient scaled by a learning rate. More advanced optimizers like Adam maintain additional state (momentum, second moments) to adapt the step size per parameter, but the fundamental idea remains the same: use gradient information to take a step in parameter space.

The optimizer step is always called after the backward pass has populated the gradient buffers. The learning rate is the single most important hyperparameter controlling step size -- too large and training diverges, too small and convergence is painfully slow. Learning rate schedules (warmup, cosine decay, step decay) dynamically adjust the learning rate during training to balance fast early progress with fine-grained later convergence.

## Math

The basic SGD parameter update rule is:

$$\theta \leftarrow \theta - \alpha \cdot g$$

With momentum $\beta$, the update becomes:

$$v \leftarrow \beta \cdot v + g$$

$$\theta \leftarrow \theta - \alpha \cdot v$$

- $\theta$ -- model parameter (weight or bias)
- $\alpha$ -- learning rate (step size)
- $g$ -- gradient $\nabla_\theta L$ of the loss with respect to $\theta$
- $v$ -- velocity (momentum buffer)
- $\beta$ -- momentum coefficient, typically $0.9$

## Key Points

- The optimizer step must be called after the backward pass and before zeroing the gradients for the next iteration.
- The learning rate $\alpha$ controls the step size: too large causes divergence, too small causes slow convergence.
- Advanced optimizers (Adam, AdaGrad, RMSProp) maintain per-parameter adaptive learning rates using gradient statistics.
- Gradient clipping is often applied before the optimizer step to prevent excessively large updates from destabilizing training.

## Function

```python
def step(w: float, grad: float, lr: float) -> float:
```

- `w` -- current parameter value $\theta$
- `grad` -- gradient of the loss with respect to `w`
- `lr` -- learning rate $\alpha$

## Run tests

```bash
pytest modules/ml/systems/optimizer-step/python -q
```
