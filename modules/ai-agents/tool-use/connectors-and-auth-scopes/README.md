# Connectors and Auth Scopes

> Track: `ai-agents` | Topic: `tool-use`

## Concept

Connectors and auth scopes govern how an agent reaches external apps such as email, calendars, docs, or CRMs without over-granting access.

## Key Points

- Connector access should request the smallest scopes that fit the action.
- Missing scopes and stale auth are different failures and should route differently.
- A connector packet should name the app, action, and required scopes before execution.

## Minimal Code Mental Model

```python
packet = connector_access_packet("gmail", "send_email", connector_scope_map)
missing = missing_connector_scopes(["gmail.read"], packet["required_scopes"])
route = connector_auth_route(authenticated=True, token_fresh=False, missing_scopes=missing)
```

## Function

```python
def connector_access_packet(
    connector: str,
    action: str,
    connector_scope_map: dict[str, dict[str, list[str]]],
) -> dict[str, object]:
def missing_connector_scopes(granted_scopes: list[str], required_scopes: list[str]) -> list[str]:
def connector_auth_route(authenticated: bool, token_fresh: bool, missing_scopes: list[str]) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/tool-use/connectors-and-auth-scopes/python -q
```
