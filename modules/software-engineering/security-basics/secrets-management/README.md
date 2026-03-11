# Secrets Management

> Track: `software-engineering` | Topic: `security-basics`

## Concept

Secrets management keeps credentials out of logs, source control, and long-lived plaintext storage by forcing them through managed injection and rotation paths.

## Key Points

- Secrets should move through managed systems instead of ad hoc files and logs.
- Output paths should distinguish deny, redact, and safe managed storage.
- Rotation rules should be explicit because stale secrets often survive unnoticed.

## Minimal Code Mental Model

```python
action = secret_handling_action("OPENAI_API_KEY", "log")
stored = managed_secret_destination("production")
rotate = secret_rotation_required(age_days=95, max_age_days=90)
```

## Function

```python
def secret_handling_action(secret_name: str, destination: str) -> str:
def managed_secret_destination(environment: str) -> str:
def secret_rotation_required(age_days: int, max_age_days: int) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/security-basics/secrets-management/python -q
```
