# Requirements And Failure Models

> Track: `software-engineering` | Topic: `system-design`

## Concept

System design starts by making quality requirements and expected failure modes explicit before choosing components.

## Key Points

- Latency, availability, and correctness trade off against each other.
- A design should be shaped by what is likely to fail, not by ideal-path diagrams.
- Overload, dependency failure, and state corruption lead to different architectural priorities.

## Minimal Code Mental Model

```python
attributes = required_quality_attributes(user_facing=True, high_scale=True, strict_correctness=False)
failure = dominant_failure_model(external_dependencies=4, stateful_components=1, overload_risk=True)
focus = architecture_focus(attributes, failure)
```

## Function

```python
def required_quality_attributes(user_facing: bool, high_scale: bool, strict_correctness: bool) -> list[str]:
def dominant_failure_model(external_dependencies: int, stateful_components: int, overload_risk: bool) -> str:
def architecture_focus(requirements: list[str], failure_model: str) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/system-design/requirements-and-failure-models/python -q
```
