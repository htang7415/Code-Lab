from __future__ import annotations

import pytest

from prompt_chaining import chain_route, chain_stages, chained_prompt


def test_prompt_chaining_builds_stages_and_messages() -> None:
    stages = chain_stages(["extract facts", "write summary", "check format"])
    assert stages == [
        {"stage_index": 0, "instruction": "extract facts", "is_last": False},
        {"stage_index": 1, "instruction": "write summary", "is_last": False},
        {"stage_index": 2, "instruction": "check format", "is_last": True},
    ]
    assert chained_prompt("facts: revenue up 12%", "write summary").startswith(
        "Previous stage output:\n"
    )


def test_prompt_chaining_routes_to_next_stage_complete_or_stop() -> None:
    assert chain_route(stage_index=0, total_stages=3, previous_success=True) == "next-stage"
    assert chain_route(stage_index=2, total_stages=3, previous_success=True) == "complete"
    assert chain_route(stage_index=1, total_stages=3, previous_success=False) == "stop"


def test_prompt_chaining_validation() -> None:
    with pytest.raises(ValueError):
        chain_stages([])
    with pytest.raises(ValueError):
        chained_prompt("", "write summary")
    with pytest.raises(ValueError):
        chain_route(stage_index=3, total_stages=3, previous_success=True)
