# Runbooks And Dashboards

> Track: `software-engineering` | Topic: `observability`

## Concept

Runbooks tell operators what to do during an incident, and dashboards tell them whether the system is moving toward or away from recovery.

## Key Points

- A dashboard without a runbook leaves responders guessing what action to take.
- A runbook without current service signals is hard to trust under pressure.
- Missing owner, rollback, or health-check information usually turns incidents into improvisation.

## Minimal Code Mental Model

```python
missing = missing_runbook_fields(runbook)
coverage = missing_dashboard_panels(["latency", "error-rate", "traffic"], ["latency", "traffic"])
ready = operator_ready(runbook, ["latency", "error-rate", "traffic"], ["latency", "error-rate", "traffic"])
```

## Function

```python
def missing_runbook_fields(runbook: dict[str, str], required_fields: list[str] | None = None) -> list[str]:
def missing_dashboard_panels(required_panels: list[str], present_panels: list[str]) -> list[str]:
def operator_ready(runbook: dict[str, str], required_panels: list[str], present_panels: list[str]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/observability/runbooks-and-dashboards/python -q
```
