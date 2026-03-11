# Least Privilege

> Track: `software-engineering` | Topic: `security-basics`

## Concept

Least privilege means granting only the scopes required for the task, then forcing review whenever a change expands access beyond that minimum.

## Key Points

- Access should be derived from required actions, not convenience.
- Scope expansion should be explicit and reviewable.
- Privilege models should make unnecessary permissions obvious in code review.

## Minimal Code Mental Model

```python
scopes = least_privilege_scopes(["read-docs", "write-docs"], capability_scopes)
extra = extra_scopes(["docs:read"], scopes)
review = privilege_escalation_required(["docs:read"], scopes)
```

## Function

```python
def least_privilege_scopes(
    requested_capabilities: list[str],
    capability_scopes: dict[str, list[str]],
) -> list[str]:
def extra_scopes(current_scopes: list[str], requested_scopes: list[str]) -> list[str]:
def privilege_escalation_required(current_scopes: list[str], requested_scopes: list[str]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/security-basics/least-privilege/python -q
```
