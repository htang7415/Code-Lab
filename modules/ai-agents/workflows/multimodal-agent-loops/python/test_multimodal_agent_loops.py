from __future__ import annotations

import pytest

from multimodal_agent_loops import (
    missing_modalities,
    multimodal_execution_route,
    multimodal_task_packet,
)


def test_multimodal_agent_loops_detect_missing_modalities_and_build_packet() -> None:
    assert missing_modalities(["text", "image"], ["text"]) == ["image"]
    assert multimodal_task_packet(
        "caption image and verify logo",
        ["text", "image"],
        ["vision_parse"],
    ) == {
        "task": "caption image and verify logo",
        "required_modalities": ["text", "image"],
        "tool_plan": ["vision_parse"],
    }


def test_multimodal_execution_route_distinguishes_request_tools_and_answer() -> None:
    assert multimodal_execution_route(["image"], ["vision_parse"]) == "request-modalities"
    assert multimodal_execution_route([], ["vision_parse"]) == "run-tools"
    assert multimodal_execution_route([], []) == "answer"


def test_multimodal_agent_loops_validation() -> None:
    with pytest.raises(ValueError):
        missing_modalities([], ["text"])
    with pytest.raises(ValueError):
        multimodal_task_packet("", ["text"], [])
    with pytest.raises(ValueError):
        multimodal_task_packet("task", [], [])
