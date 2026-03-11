from __future__ import annotations


def secret_handling_action(secret_name: str, destination: str) -> str:
    if not secret_name.strip():
        raise ValueError("secret_name must be non-empty")

    normalized_destination = destination.strip().lower()
    if normalized_destination in {"log", "ticket", "source-control"}:
        return "deny"
    if normalized_destination in {"config-file", "terminal-output"}:
        return "redact"
    if normalized_destination == "process-env":
        return "inject-ephemeral"
    if normalized_destination == "secret-manager":
        return "store-managed"
    raise ValueError("unknown destination")


def managed_secret_destination(environment: str) -> str:
    normalized_environment = environment.strip().lower()
    if normalized_environment in {"prod", "production", "staging"}:
        return "secret-manager"
    if normalized_environment in {"local", "dev", "development", "test"}:
        return "process-env"
    raise ValueError("unknown environment")


def secret_rotation_required(age_days: int, max_age_days: int) -> bool:
    if age_days < 0 or max_age_days <= 0:
        raise ValueError("ages must be positive")
    return age_days >= max_age_days
