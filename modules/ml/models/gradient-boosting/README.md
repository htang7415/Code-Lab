# Gradient Boosting Step

> Track: `ml` | Topic: `models`

## Concept

Gradient boosting fits a weak learner to the current residual signal and updates predictions in small steps.
This module uses squared-error residuals to show the basic stage-wise update.

## Math

$$r_i = y_i - \hat{y}_i$$

$$\hat{y}_i' = \hat{y}_i + \eta \, h_i$$

- $r_i$ -- residual for example $i$
- $y_i$ -- target value
- $\hat{y}_i$ -- current prediction
- $h_i$ -- weak learner output
- $\eta$ -- learning rate

## Key Points

- Boosting corrects current errors instead of refitting from scratch.
- Small learning rates make stage-wise updates more stable.
- For squared error, fitting residuals matches the negative gradient.

## Function

```python
def gradient_boosting_step(
    targets: list[float],
    predictions: list[float],
    weak_learner_output: list[float],
    learning_rate: float,
) -> tuple[list[float], list[float]]:
```

## Run tests

```bash
pytest modules/ml/models/gradient-boosting/python -q
```
