from __future__ import annotations

import pytest

from connectors_and_auth_scopes import (
    connector_access_packet,
    connector_auth_route,
    missing_connector_scopes,
)


def test_connector_access_packet_and_missing_scopes() -> None:
    connector_scope_map = {
        "gmail": {
            "read_email": ["gmail.read"],
            "send_email": ["gmail.send", "contacts.read"],
        },
        "calendar": {
            "create_event": ["calendar.write"],
        },
    }

    packet = connector_access_packet("gmail", "send_email", connector_scope_map)
    assert packet == {
        "connector": "gmail",
        "action": "send_email",
        "required_scopes": ["contacts.read", "gmail.send"],
    }
    assert missing_connector_scopes(["gmail.send"], packet["required_scopes"]) == ["contacts.read"]


def test_connector_auth_route_distinguishes_auth_scope_and_refresh_failures() -> None:
    assert connector_auth_route(authenticated=False, token_fresh=True, missing_scopes=[]) == "reauth"
    assert connector_auth_route(authenticated=True, token_fresh=True, missing_scopes=["gmail.send"]) == "request-scopes"
    assert connector_auth_route(authenticated=True, token_fresh=False, missing_scopes=[]) == "refresh-token"
    assert connector_auth_route(authenticated=True, token_fresh=True, missing_scopes=[]) == "execute"


def test_connectors_and_auth_scopes_validation() -> None:
    with pytest.raises(ValueError):
        connector_access_packet("", "send_email", {"gmail": {"send_email": ["gmail.send"]}})
    with pytest.raises(ValueError):
        connector_access_packet("gmail", "send_email", {})
    with pytest.raises(ValueError):
        connector_access_packet("gmail", "delete_account", {"gmail": {"send_email": ["gmail.send"]}})
    with pytest.raises(ValueError):
        missing_connector_scopes(["gmail.send"], [])
