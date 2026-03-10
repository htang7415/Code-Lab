# Training Loop Mechanics

> Track: `ml` | Topic: `systems`

## Purpose

Use this module to learn the core moving parts of a modern training loop in one
place: zeroing gradients, forward and backward passes, optimizer updates,
gradient accumulation, mixed precision, and basic gradient sanity checks.

## First Principles

- Training is an ordered state-update loop, not a black box.
- The forward pass computes outputs with current parameters.
- The backward pass turns loss into gradients.
- The optimizer step applies those gradients to parameters.
- Gradient accumulation and mixed precision change how the loop is executed, not the learning objective itself.

## Core Math

Affine forward step:

$$
z = w^\top x + b
$$

Backward local gradient:

$$
\frac{\partial L}{\partial w} = \frac{\partial L}{\partial y}\frac{\partial y}{\partial w}
$$

SGD update:

$$
\theta \leftarrow \theta - \eta g
$$

Accumulated gradient:

$$
g_{\text{eff}} = \frac{1}{K}\sum_{k=1}^{K} g_k
$$

## Minimal Code Mental Model

```python
grads = zero_grad(grads)
logit = forward(x, w, b)
grad = backward(dy, x_cached)
accumulated = accumulate(micro_batch_grads)
scaled = scale_gradients(accumulated, scale=1024.0)
if gradients_ok(scaled):
    w = step(w, grad=scaled[0], lr=1e-3)
```

## Functions

```python
def zero_grad(grads: list[float]) -> list[float]:
def forward(x: list[float], w: list[float], b: float) -> float:
def backward(dy: float, x: float) -> float:
def step(w: float, grad: float, lr: float) -> float:
def accumulate(grads: list[list[float]]) -> list[float]:
def scale_gradients(grads: list[float], scale: float) -> list[float]:
def gradients_ok(grads: list[float]) -> bool:
```

## When To Use What

- Use `zero_grad` when each optimization step should start from a clean gradient buffer.
- Use `accumulate` when memory is too small for the desired effective batch size.
- Use `scale_gradients` inside mixed-precision training loops when FP16 underflow is a risk.
- Use `gradients_ok` as a cheap sanity check when debugging dead, NaN, or disconnected gradients.

## Run tests

```bash
pytest modules/ml/systems/training-loop-mechanics/python -q
```
