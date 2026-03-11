# Cost-Performance Tradeoffs

> Track: `software-engineering` | Topic: `performance`

## Concept

Performance changes should be judged against their cost, because lower latency is only one part of the engineering decision.

## Key Points

- Faster is not automatically better if the cost increase is too large.
- Compare improvements in units the team can reason about, like milliseconds saved and cost per 1k requests.
- Small latency wins on low-value paths often do not justify large infrastructure spend.

## Minimal Code Mental Model

```python
cost = cost_per_1k_requests(hourly_cost=12.0, requests_per_hour=60000)
gain = latency_improvement_ms(baseline_ms=300, candidate_ms=220)
worth_it = worthwhile_tradeoff(gain, extra_cost_per_1k=0.02, max_extra_cost_per_1k=0.03)
```

## Function

```python
def cost_per_1k_requests(hourly_cost: float, requests_per_hour: int) -> float:
def latency_improvement_ms(baseline_ms: int, candidate_ms: int) -> int:
def worthwhile_tradeoff(
    latency_gain_ms: int,
    extra_cost_per_1k: float,
    max_extra_cost_per_1k: float,
) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/performance/cost-performance-tradeoffs/python -q
```
