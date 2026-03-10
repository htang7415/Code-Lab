# Capacity Stress Metrics

> Track: `ml` | Topic: `mlops`

## Purpose

Use this module to summarize whether a serving system is below capacity,
routinely breaching it, or collapsing into a severe tail.

## First Principles

- Capacity problems are about both frequency and severity.
- A breach rate tells you how often the system fails the target.
- Margin and pressure metrics tell you how bad the failure is.
- Bucket metrics are second-order summaries for the shape of overload severity.

## Core Math

- Breach rate:
  $$
  \frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[x_i > C]
  $$
- Overload margin:
  $$
  \frac{1}{N}\sum_{i=1}^{N}\max(0, x_i - C)
  $$
- Pressure score:
  $$
  \frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[x_i > C]\left(1 + \frac{x_i - C}{C}\right)
  $$

## Minimal Code Mental Model

```python
breaches, rate = capacity_breach_rate(observations, capacity)
pressure = pressure_score(observations, capacity)
```

## Function

```python
def capacity_breach_rate(observations: list[float], capacity: float) -> tuple[int, float]:
def headroom_gap(observations: list[float], ceiling: float) -> tuple[list[float], float]:
def overload_margin(observations: list[float], capacity: float) -> float:
def pressure_score(observations: list[float], capacity: float) -> float:
def surge_pressure(observations: list[float], capacity: float) -> float:
def breach_bucket_share(observations: list[float], capacity: float, cutoffs: list[float]) -> list[float]:
def breach_bucket_entropy(observations: list[float], capacity: float, cutoffs: list[float]) -> float:
def breach_bucket_slope(observations: list[float], capacity: float, cutoffs: list[float]) -> float:
def breach_bucket_tail(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
    tail_buckets: int = 1,
) -> float:
```

## When To Use What

- Use breach rate as the first capacity health number.
- Use headroom gap when you want to know how close the system usually is to the ceiling.
- Use overload margin or pressure score when severity matters, not just frequency.
- Use breach-bucket metrics when you need the shape of overload, not just its average.

## Run tests

```bash
pytest modules/ml/mlops/capacity-stress-metrics/python -q
```
