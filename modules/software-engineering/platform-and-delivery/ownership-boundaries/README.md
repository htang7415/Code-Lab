# Ownership Boundaries

> Track: `software-engineering` | Topic: `platform-and-delivery`

## Concept

Ownership boundaries are healthy when teams know who decides, who operates, and who changes a system without repeated ambiguity or excess handoffs.

## Key Points

- Shared ownership without clear decision rights usually slows delivery.
- Frequent cross-team handoffs are a sign the boundary may be wrong or under-specified.
- A good boundary reduces coordination cost without hiding critical responsibilities.

## Minimal Code Mental Model

```python
model = ownership_model(single_team_owner=True, many_consumers=True)
health = boundary_health(shared_services=2, cross_team_handoffs=1, ambiguous_owner=False)
escalate = escalation_needed(shared_services=5, cross_team_handoffs=4, ambiguous_owner=True)
```

## Function

```python
def ownership_model(single_team_owner: bool, many_consumers: bool) -> str:
def boundary_health(shared_services: int, cross_team_handoffs: int, ambiguous_owner: bool) -> str:
def escalation_needed(shared_services: int, cross_team_handoffs: int, ambiguous_owner: bool) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/platform-and-delivery/ownership-boundaries/python -q
```
