# ML Monitoring

Monitoring is how you detect that a deployed model is still serving traffic but no longer serving value.

## Purpose

Use this page to organize monitoring into:
- data drift
- prediction drift
- service health
- reliability budgets

## First Principles

- Not every metric movement matters; the important question is whether users are being harmed.
- Data drift, prediction drift, and serving failures are different failure classes.
- Global averages often hide slice failures, queue buildup, and tail latency.
- Error budgets help connect model quality, rollout speed, and operational reliability.

## Core Math

- PSI-style drift:
  $$
  \sum_i (p_i - q_i)\log\frac{p_i}{q_i}
  $$
- SLA compliance:
  $$
  \frac{\#\{\text{requests within target}\}}{\#\{\text{requests}\}}
  $$

## Minimal Code Mental Model

```python
if drift_score > threshold or tail_latency > budget:
    alert()
```

## Canonical Modules

- Data drift: `feature-drift-psi`, `drift-detection`
- Prediction quality: `prediction-monitoring`
- Service health: `request-sla`, `queue-age-percentiles`, `saturation-rate`
- Reliability budget: `error-budget`

## When To Use What

- Use drift metrics when the input distribution is changing.
- Use prediction monitoring when labels or proxy outcomes arrive after deployment.
- Use queue and SLA metrics when latency is part of product quality.
- Use `error-budget` when you need a single reliability constraint that gates rollout speed.
