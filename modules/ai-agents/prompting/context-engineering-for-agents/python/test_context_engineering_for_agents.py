from __future__ import annotations

import pytest

from context_engineering_for_agents import (
    available_context_budget,
    pack_context_blocks,
    rank_context_blocks,
)


def test_context_engineering_ranks_and_packs_blocks_under_budget() -> None:
    budget = available_context_budget(context_window=8192, reserved_output_tokens=1024)
    assert budget == 7168

    ranked = rank_context_blocks(
        [
            {"name": "memory-summary", "tokens": 400, "priority": 2},
            {"name": "retrieved-evidence", "tokens": 1200, "priority": 3},
            {"name": "style-guide", "tokens": 600, "priority": 1},
        ]
    )
    assert [block["name"] for block in ranked] == [
        "retrieved-evidence",
        "memory-summary",
        "style-guide",
    ]
    assert pack_context_blocks(ranked, token_budget=1600) == [
        "retrieved-evidence",
        "memory-summary",
    ]


def test_context_engineering_validation() -> None:
    with pytest.raises(ValueError):
        available_context_budget(context_window=1024, reserved_output_tokens=1024)
    with pytest.raises(ValueError):
        rank_context_blocks([])
    with pytest.raises(ValueError):
        rank_context_blocks([{"name": "", "tokens": 10, "priority": 1}])
    with pytest.raises(ValueError):
        pack_context_blocks([{"name": "memory", "tokens": 0, "priority": 1}], token_budget=100)
