from __future__ import annotations

import pytest

from voice_and_realtime_agent_loops import (
    realtime_budget_ok,
    realtime_route,
    voice_turn_packet,
)


def test_voice_and_realtime_loops_build_turn_packet_and_routes() -> None:
    assert voice_turn_packet("audio", transcript="schedule meeting tomorrow", interrupted=False) == {
        "input_mode": "audio",
        "transcript": "schedule meeting tomorrow",
        "interrupted": False,
    }
    assert realtime_budget_ok(latency_ms=180, max_latency_ms=250) is True
    assert realtime_route(has_transcript=True, interrupted=False, needs_tool=True) == "run-tool"


def test_voice_and_realtime_loops_distinguish_wait_yield_and_respond() -> None:
    assert realtime_route(has_transcript=False, interrupted=False, needs_tool=False) == "wait"
    assert realtime_route(has_transcript=True, interrupted=True, needs_tool=False) == "yield"
    assert realtime_route(has_transcript=True, interrupted=False, needs_tool=False) == "respond"


def test_voice_and_realtime_loops_validation() -> None:
    with pytest.raises(ValueError):
        voice_turn_packet("video", transcript="hello")
    with pytest.raises(ValueError):
        voice_turn_packet("audio", transcript=None, interrupted=False)
    with pytest.raises(ValueError):
        realtime_budget_ok(latency_ms=-1, max_latency_ms=250)
