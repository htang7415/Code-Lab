from __future__ import annotations


def least_privilege_scopes(
    requested_capabilities: list[str],
    capability_scopes: dict[str, list[str]],
) -> list[str]:
    if not requested_capabilities:
        raise ValueError("requested_capabilities must be non-empty")

    scopes: set[str] = set()
    for capability in requested_capabilities:
        cleaned_capability = capability.strip()
        if not cleaned_capability:
            raise ValueError("requested capabilities must be non-empty")
        if cleaned_capability not in capability_scopes:
            raise ValueError(f"unknown capability: {cleaned_capability}")
        scopes.update(scope.strip() for scope in capability_scopes[cleaned_capability] if scope.strip())
    return sorted(scopes)


def extra_scopes(current_scopes: list[str], requested_scopes: list[str]) -> list[str]:
    current = {scope.strip() for scope in current_scopes if scope.strip()}
    requested = {scope.strip() for scope in requested_scopes if scope.strip()}
    return sorted(requested - current)


def privilege_escalation_required(
    current_scopes: list[str],
    requested_scopes: list[str],
) -> bool:
    if not [scope for scope in requested_scopes if scope.strip()]:
        raise ValueError("requested_scopes must be non-empty")
    return bool(extra_scopes(current_scopes, requested_scopes))
