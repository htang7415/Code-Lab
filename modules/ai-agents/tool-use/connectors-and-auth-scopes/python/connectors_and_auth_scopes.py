from __future__ import annotations


def connector_access_packet(
    connector: str,
    action: str,
    connector_scope_map: dict[str, dict[str, list[str]]],
) -> dict[str, object]:
    cleaned_connector = connector.strip()
    cleaned_action = action.strip()
    if not cleaned_connector:
        raise ValueError("connector must be non-empty")
    if not cleaned_action:
        raise ValueError("action must be non-empty")
    if cleaned_connector not in connector_scope_map:
        raise ValueError(f"unknown connector: {cleaned_connector}")

    action_map = connector_scope_map[cleaned_connector]
    if cleaned_action not in action_map:
        raise ValueError(f"unknown action for connector: {cleaned_action}")

    scopes = sorted({scope.strip() for scope in action_map[cleaned_action] if scope.strip()})
    return {
        "connector": cleaned_connector,
        "action": cleaned_action,
        "required_scopes": scopes,
    }


def missing_connector_scopes(granted_scopes: list[str], required_scopes: list[str]) -> list[str]:
    granted = {scope.strip() for scope in granted_scopes if scope.strip()}
    required = {scope.strip() for scope in required_scopes if scope.strip()}
    if not required:
        raise ValueError("required_scopes must be non-empty")
    return sorted(required - granted)


def connector_auth_route(authenticated: bool, token_fresh: bool, missing_scopes: list[str]) -> str:
    if not authenticated:
        return "reauth"
    if missing_scopes:
        return "request-scopes"
    if not token_fresh:
        return "refresh-token"
    return "execute"
