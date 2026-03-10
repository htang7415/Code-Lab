from __future__ import annotations

import pytest

from tool_use_basics import select_tool, tool_call, tool_result


def test_select_tool_uses_keyword_overlap() -> None:
    tool_keywords = {
        "weather": ["weather", "temperature", "forecast"],
        "calendar": ["calendar", "meeting", "schedule"],
    }
    assert select_tool("check the weather forecast", tool_keywords) == "weather"
    assert select_tool("schedule a meeting", tool_keywords) == "calendar"


def test_tool_call_and_result_build_structured_messages() -> None:
    call = tool_call("weather", {"location": "Madison, WI"}, call_id="call_7")
    assert call["type"] == "tool_call"
    assert call["name"] == "weather"
    result = tool_result("call_7", {"temperature_f": 41})
    assert result == {
        "type": "tool_result",
        "call_id": "call_7",
        "output": {"temperature_f": 41},
        "is_error": False,
    }


def test_tool_message_validation_rejects_empty_ids_or_names() -> None:
    with pytest.raises(ValueError):
        tool_call("", {})
    with pytest.raises(ValueError):
        tool_result("", {})
