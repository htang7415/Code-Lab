# Profiling Workflow

> Track: `software-engineering` | Topic: `performance`

## Concept

A profiling workflow turns a performance complaint into a measured bottleneck and then into the next investigation step.

## Key Points

- The first question is where the time or resources go, not how to optimize yet.
- CPU, I/O, and allocation bottlenecks need different fixes.
- The highest-cost function or subsystem is usually the first place to inspect.

## Minimal Code Mental Model

```python
bottleneck = bottleneck_type(cpu_pct=75, io_wait_pct=10, alloc_pct=15)
target = highest_cost_function({"render": 12.0, "query_db": 80.0, "serialize": 8.0})
next_step = next_profiling_step(bottleneck)
```

## Function

```python
def bottleneck_type(cpu_pct: float, io_wait_pct: float, alloc_pct: float) -> str:
def highest_cost_function(profile_costs_ms: dict[str, float]) -> str:
def next_profiling_step(bottleneck: str) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/performance/profiling-workflow/python -q
```
