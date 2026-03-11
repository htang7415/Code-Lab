from __future__ import annotations

import pytest

from least_privilege import extra_scopes, least_privilege_scopes, privilege_escalation_required


def test_least_privilege_collects_only_required_scopes() -> None:
    capability_scopes = {
        "read-docs": ["docs:read"],
        "write-docs": ["docs:read", "docs:write"],
        "manage-secrets": ["secrets:read"],
    }

    assert least_privilege_scopes(["read-docs", "write-docs"], capability_scopes) == [
        "docs:read",
        "docs:write",
    ]


def test_extra_scopes_reports_only_new_permissions() -> None:
    assert extra_scopes(["docs:read"], ["docs:read", "docs:write"]) == ["docs:write"]
    assert extra_scopes(["docs:read"], ["docs:read"]) == []


def test_privilege_escalation_required_flags_scope_expansion() -> None:
    assert privilege_escalation_required(["docs:read"], ["docs:read"]) is False
    assert privilege_escalation_required(["docs:read"], ["docs:read", "docs:write"]) is True

    with pytest.raises(ValueError):
        privilege_escalation_required(["docs:read"], [])
