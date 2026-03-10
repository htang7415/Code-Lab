# Gradient Boosting Step

> Track: `ml` | Topic: `models`

## Purpose

Use this module to understand the core stage-wise update behind gradient
boosting for regression.

## First Principles

- Boosting improves a model by correcting current errors instead of refitting from scratch.
- At each stage, a weak learner fits the residual or negative gradient.
- Small learning rates make boosting more stable and usually require more stages.
- For squared error, residual fitting is the same as fitting the negative gradient.

## Core Math

$$
r_i = y_i - \hat{y}_i
$$

$$
\hat{y}_i' = \hat{y}_i + \eta \, h_i
$$

- $r_i$ -- residual for example $i$
- $y_i$ -- target value
- $\hat{y}_i$ -- current prediction
- $h_i$ -- weak learner output
- $\eta$ -- learning rate

## Minimal Code Mental Model

```python
residuals, updated = gradient_boosting_step(
    targets,
    predictions,
    weak_learner_output,
    learning_rate,
)
```

## Function

```python
def gradient_boosting_step(
    targets: list[float],
    predictions: list[float],
    weak_learner_output: list[float],
    learning_rate: float,
) -> tuple[list[float], list[float]]:
```

## When To Use What

- Use this module to understand the boosting update before XGBoost-style second-order variants.
- Use small learning rates when you want more stable stage-wise improvement.
- Pair this with tree-based weak learners when studying practical boosting systems.

## Run tests

```bash
pytest modules/ml/models/gradient-boosting/python -q
```
