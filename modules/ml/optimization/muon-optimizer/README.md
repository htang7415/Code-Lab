# Muon Optimizer

> Track: `ml` | Topic: `optimization`

## Concept

Muon is a matrix-aware optimizer: it applies momentum, then orthogonalizes the
2D update so its directions stay well-conditioned. Practical implementations
orthogonalize each matrix update (often via Newton-Schulz iterations). This
module uses a tiny Gram-Schmidt approximation for a learnable demo.

## Math

- $m_t = \beta m_{t-1} + g_t$
- $Q_t = \mathrm{orthogonalize}(m_t)$
- $W_{t+1} = W_t - \eta Q_t$

- $\beta$ -- momentum coefficient
- $m_t$ -- momentum at step $t$
- $g_t$ -- gradient at step $t$
- $Q_t$ -- orthogonalized update at step $t$
- $W_t$ -- weight matrix at step $t$
- $\eta$ -- learning rate (step size)

## Function

```python
def muon_step(
    weights: list[list[float]],
    grad: list[list[float]],
    velocity: list[list[float]] | None,
    lr: float = 0.1,
    momentum: float = 0.9,
) -> tuple[list[list[float]], list[list[float]]]:
```

## Demo code

```python
weights = [[1.0, -1.0], [0.5, 0.25]]
grad = [[0.2, -0.1], [0.05, 0.4]]
new_weights, velocity = muon_step(weights, grad, None, lr=0.1, momentum=0.9)
```

## Run tests

```bash
pytest modules/ml/optimization/muon-optimizer/python -q
cargo test --manifest-path modules/ml/optimization/muon-optimizer/rust/Cargo.toml
```
