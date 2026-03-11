from __future__ import annotations

import pytest

from secrets_management import (
    managed_secret_destination,
    secret_handling_action,
    secret_rotation_required,
)


def test_secret_handling_distinguishes_deny_redact_and_managed_paths() -> None:
    assert secret_handling_action("OPENAI_API_KEY", "log") == "deny"
    assert secret_handling_action("OPENAI_API_KEY", "config-file") == "redact"
    assert secret_handling_action("OPENAI_API_KEY", "secret-manager") == "store-managed"
    assert secret_handling_action("OPENAI_API_KEY", "process-env") == "inject-ephemeral"


def test_managed_secret_destination_depends_on_environment() -> None:
    assert managed_secret_destination("production") == "secret-manager"
    assert managed_secret_destination("dev") == "process-env"


def test_secret_rotation_required_flags_expired_credentials() -> None:
    assert secret_rotation_required(age_days=95, max_age_days=90) is True
    assert secret_rotation_required(age_days=30, max_age_days=90) is False

    with pytest.raises(ValueError):
        secret_rotation_required(age_days=-1, max_age_days=90)
