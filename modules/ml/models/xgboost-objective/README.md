# XGBoost Split Gain

> Track: `ml` | Topic: `models`

## Concept

XGBoost chooses splits by comparing the second-order objective improvement from the left and right child nodes against the unsplit parent.

## Math

$$\mathrm{Gain} = \frac{1}{2}
\left(
\frac{G_L^2}{H_L + \lambda}
+ \frac{G_R^2}{H_R + \lambda}
- \frac{(G_L + G_R)^2}{H_L + H_R + \lambda}
\right) - \gamma$$

- $G_L, G_R$ -- summed first-order gradients in the left and right nodes
- $H_L, H_R$ -- summed second-order gradients in the left and right nodes
- $\lambda$ -- L2 leaf regularization
- $\gamma$ -- split penalty

## Key Points

- Larger gain means a more useful split.
- Hessians scale how confident the objective is around current predictions.
- The split penalty $\gamma$ suppresses weak splits.

## Function

```python
def split_gain(
    left_grad: float,
    left_hess: float,
    right_grad: float,
    right_hess: float,
    lambda_reg: float,
    gamma: float,
) -> float:
```

## Run tests

```bash
pytest modules/ml/models/xgboost-objective/python -q
```
