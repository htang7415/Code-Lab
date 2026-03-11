from __future__ import annotations

import pytest

from mcp import (
    prompt_get_request,
    resource_read_request,
    server_capabilities,
    session_context,
    tool_call_request,
    transport_roles,
)


def test_mcp_helpers_capture_roles_capabilities_and_requests() -> None:
    assert transport_roles("agent", "desktop app", "filesystem server") == {
        "client": "agent",
        "host": "desktop app",
        "server": "filesystem server",
    }
    assert server_capabilities(tool_count=3, resource_count=0, prompt_count=1, auth_required=True) == {
        "tools": True,
        "resources": False,
        "prompts": True,
        "auth": True,
    }
    assert session_context("sess_7", ["repo:read", "repo:read"], authenticated=True) == {
        "session_id": "sess_7",
        "scopes": ["repo:read"],
        "authenticated": True,
    }
    assert resource_read_request("repo://README.md", "sess_7") == {
        "method": "resources/read",
        "params": {"uri": "repo://README.md", "session_id": "sess_7"},
    }
    assert prompt_get_request("summarize_diff", {"style": "concise"}, "sess_7") == {
        "method": "prompts/get",
        "params": {
            "name": "summarize_diff",
            "arguments": {"style": "concise"},
            "session_id": "sess_7",
        },
    }
    assert tool_call_request("search", {"query": "MCP"}, "sess_7") == {
        "method": "tools/call",
        "params": {"name": "search", "arguments": {"query": "MCP"}, "session_id": "sess_7"},
    }


def test_mcp_validation_rejects_invalid_names_or_counts() -> None:
    with pytest.raises(ValueError):
        server_capabilities(tool_count=-1)
    with pytest.raises(ValueError):
        transport_roles("", "desktop app", "filesystem server")
    with pytest.raises(ValueError):
        session_context("", ["repo:read"], authenticated=True)
    with pytest.raises(ValueError):
        resource_read_request("", "sess_7")
    with pytest.raises(ValueError):
        prompt_get_request("", {}, "sess_7")
    with pytest.raises(ValueError):
        tool_call_request("", {}, "sess_7")
    with pytest.raises(ValueError):
        tool_call_request("search", {}, "")
