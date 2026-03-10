# Binary Rate Comparison Metrics

> Track: `ml` | Topic: `evaluation`

## Concept

Binary rate comparison metrics summarize how often a positive event happens and how that rate changes across groups or baselines.

This family groups:

- raw positive rates
- additive differences such as gaps and deltas
- multiplicative comparisons such as ratios
- odds transforms
- log-space versions of ratio metrics

## Why Learn Them Together

- They all start from the same primitive: the positive event rate.
- Most naming differences are domain conventions rather than new math.
- Log transforms are the additive view of multiplicative effects.

## Core Functions

```python
def positive_rate(labels: list[int]) -> float:
def base_rate_gap(group_a: list[int], group_b: list[int]) -> float:
def prevalence_delta(baseline_labels: list[int], comparison_labels: list[int]) -> float:
def prevalence_ratio(group_a: list[int], group_b: list[int]) -> float:
def prevalence_index(labels: list[int], baseline_rate: float) -> float:
def prevalence_odds(labels: list[int]) -> float:
def log_prevalence_ratio(group_a: list[int], group_b: list[int]) -> float:
def log_rate_ratio(event_count: int, total_count: int, baseline_event_count: int, baseline_total_count: int) -> float:
```

## Naming Equivalences

- `risk_ratio` and `base_rate_ratio` are the same multiplicative comparison as `prevalence_ratio`.
- `log_risk_ratio` and `log_relative_risk` are the same log-space comparison as `log_prevalence_ratio`.

## Comparison

| Metric family | Question answered |
| --- | --- |
| Positive rate | How common is the positive outcome? |
| Gap / delta | How much higher or lower is one group in absolute terms? |
| Ratio | How many times larger is one rate than another? |
| Odds | How large is the positive rate relative to the negative rate? |
| Log ratio | What is the additive effect size of a multiplicative comparison? |

## Key Points

- Use gaps when absolute change matters.
- Use ratios when relative lift matters.
- Use log ratios when you need additive comparisons or symmetric positive and negative effects.
- Watch the zero-rate edge cases because ratios and logs can become infinite.

## Run tests

```bash
pytest modules/ml/evaluation/binary-rate-comparison-metrics/python -q
```
