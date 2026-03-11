# Cognitive Load And Team Interfaces

> Track: `software-engineering` | Topic: `platform-and-delivery`

## Concept

Team boundaries work best when a team can understand its own systems without constant coordination across blurry ownership lines.

## Key Points

- Cognitive load is a real limit, not a soft preference.
- Shared ownership often looks flexible at first and expensive later.
- Team interfaces should make dependencies and escalation paths obvious.

## Minimal Code Mental Model

```python
load = team_cognitive_load(services=5, workflows=4, pager_domains=3)
clarity = interface_clarity(owned_components=4, shared_components=1)
assert boundary_rework_needed(load, clarity) is True
```

## Function

```python
def team_cognitive_load(services: int, workflows: int, pager_domains: int) -> str:
def interface_clarity(owned_components: int, shared_components: int) -> str:
def boundary_rework_needed(load: str, clarity: str) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/platform-and-delivery/cognitive-load-and-team-interfaces/python -q
```
