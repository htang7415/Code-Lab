# Async Python Services

> Track: `software-engineering` | Topic: `python`

## Concept

Async Python services are most useful when request time is dominated by external waiting rather than local CPU-bound work.

## Key Points

- Async improves throughput for I/O-bound services, not for every Python workload.
- Concurrency still needs explicit limits.
- Backpressure matters when in-flight work exceeds the service budget.

## Minimal Code Mental Model

```python
fit = async_service_fit(network_wait_ms=120, cpu_ms=20)
budget = concurrency_budget(worker_count=4, per_worker_in_flight=25)
backpressure = backpressure_needed(in_flight=120, budget=100)
```

## Function

```python
def async_service_fit(network_wait_ms: int, cpu_ms: int) -> bool:
def concurrency_budget(worker_count: int, per_worker_in_flight: int) -> int:
def backpressure_needed(in_flight: int, budget: int) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/python/async-python-services/python -q
```
