# Incidents And Postmortems

> Track: `software-engineering` | Topic: `reliability`

## Concept

Incident response limits user harm in the moment, and the postmortem turns the event into concrete follow-up work that reduces repeat failures.

## Key Points

- Severity should reflect user harm and data risk, not internal embarrassment.
- A postmortem is incomplete if key timeline or remediation details are missing.
- Follow-up work matters more than blame assignment.

## Minimal Code Mental Model

```python
severity = incident_severity(user_impacting=True, duration_minutes=45, data_loss=False)
missing = missing_postmortem_sections(postmortem)
complete = postmortem_complete(postmortem, action_items=["add retry budget alert"])
```

## Function

```python
def incident_severity(user_impacting: bool, duration_minutes: int, data_loss: bool) -> str:
def missing_postmortem_sections(
    postmortem: dict[str, str],
    required_sections: list[str] | None = None,
) -> list[str]:
def postmortem_complete(postmortem: dict[str, str], action_items: list[str]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/reliability/incidents-and-postmortems/python -q
```
