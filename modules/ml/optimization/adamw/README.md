# AdamW

> Track: `ml` | Topic: `optimization`

## Concept

AdamW decouples weight decay from adaptive updates.

## Math
$$w_{t+1} = w_t - \eta \frac{m_t}{\sqrt{v_t}+\epsilon} - \eta \lambda w_t$$

- $\eta$ -- learning rate (step size)
- $\epsilon$ -- small constant for numerical stability
- $\lambda$ -- regularization strength or weighting coefficient
- $w_t$ -- weight parameter at step t
- $m_t$ -- first moment (momentum) at step t
- $v_t$ -- second moment (variance) at step t
- $w$ -- weight parameter
- $t$ -- timestep or iteration

- $m$ -- first moment (momentum)
- $v$ -- second moment (variance)

## Function

```python
def adamw_step(w: float, grad: float, m: float, v: float, lr: float, wd: float, beta1: float, beta2: float, eps: float) -> tuple[float, float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/adamw/python -q
```