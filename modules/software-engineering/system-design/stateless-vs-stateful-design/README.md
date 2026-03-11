# Stateless Vs Stateful Design

> Track: `software-engineering` | Topic: `system-design`

## Concept

Stateless components are easier to scale and replace, while stateful components can provide stronger locality or coordination at the cost of harder recovery.

## Key Points

- Stateless services are usually easier to load-balance horizontally.
- Local mutable state makes failover and scaling more complicated.
- State should live where recovery and consistency rules are explicit.

## Minimal Code Mental Model

```python
style = component_style(needs_durable_session=True, requires_local_cache_consistency=False)
scaling = horizontal_scaling_ease(style)
recovery = recovery_complexity(style)
```

## Function

```python
def component_style(needs_durable_session: bool, requires_local_cache_consistency: bool) -> str:
def horizontal_scaling_ease(style: str) -> str:
def recovery_complexity(style: str) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/system-design/stateless-vs-stateful-design/python -q
```
