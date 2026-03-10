from __future__ import annotations

import pytest

from mcp import server_capabilities, tool_call_request, tool_descriptor


def test_mcp_helpers_capture_server_capabilities_and_tool_calls() -> None:
    assert server_capabilities(tool_count=3, resource_count=0, prompt_count=1) == {
        "tools": True,
        "resources": False,
        "prompts": True,
    }
    assert tool_descriptor("search", "Search documents") == {
        "name": "search",
        "description": "Search documents",
    }
    assert tool_call_request("search", {"query": "MCP"}) == {
        "method": "tools/call",
        "params": {"name": "search", "arguments": {"query": "MCP"}},
    }


def test_mcp_validation_rejects_invalid_names_or_counts() -> None:
    with pytest.raises(ValueError):
        server_capabilities(tool_count=-1)
    with pytest.raises(ValueError):
        tool_descriptor("", "desc")
    with pytest.raises(ValueError):
        tool_call_request("", {})
