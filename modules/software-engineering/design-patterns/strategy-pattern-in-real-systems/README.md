# Strategy Pattern In Real Systems

> Track: `software-engineering` | Topic: `design-patterns`

## Concept

Strategy is useful when one stable interface needs multiple policy choices, such as selecting a deployment region by latency or by cost.

## Key Points

- The caller should not change when the policy changes.
- Different strategies often optimize different production constraints.
- Use strategy for policy selection, not for hiding ordinary conditionals.

## Minimal Code Mental Model

```python
candidates = [
    {"name": "us-east", "latency_ms": 40, "monthly_cost": 200},
    {"name": "eu-west", "latency_ms": 60, "monthly_cost": 120},
]
assert select_region(candidates, lowest_latency) == "us-east"
assert select_region(candidates, lowest_cost) == "eu-west"
```

## Function

```python
def lowest_latency(candidates: list[dict[str, int | str]]) -> dict[str, int | str]:
def lowest_cost(candidates: list[dict[str, int | str]]) -> dict[str, int | str]:
def select_region(candidates: list[dict[str, int | str]], strategy) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/design-patterns/strategy-pattern-in-real-systems/python -q
```
