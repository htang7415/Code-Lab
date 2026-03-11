from __future__ import annotations

import pytest

from terminal_use import (
    DEFAULT_DESTRUCTIVE_MARKERS,
    terminal_command_risk,
    terminal_packet,
    terminal_route,
)


def test_terminal_use_classifies_command_risk() -> None:
    assert terminal_command_risk("rm -rf build", DEFAULT_DESTRUCTIVE_MARKERS) == "high"
    assert terminal_command_risk("sudo apt install ripgrep", DEFAULT_DESTRUCTIVE_MARKERS) == "medium"
    assert terminal_command_risk("rg -n TODO .", DEFAULT_DESTRUCTIVE_MARKERS) == "low"


def test_terminal_use_builds_packet_and_routes_execution() -> None:
    assert terminal_packet("rg -n TODO .", cwd="/repo", expect_json=False) == {
        "command": "rg -n TODO .",
        "cwd": "/repo",
        "expect_json": False,
    }
    assert terminal_route("low", has_dry_run=True) == "execute"
    assert terminal_route("medium", has_dry_run=True) == "dry-run"
    assert terminal_route("medium", has_dry_run=False) == "review"
    assert terminal_route("high", has_dry_run=True) == "review"


def test_terminal_use_validation() -> None:
    with pytest.raises(ValueError):
        terminal_command_risk("", DEFAULT_DESTRUCTIVE_MARKERS)
    with pytest.raises(ValueError):
        terminal_packet("rg -n TODO .", cwd=" ")
    with pytest.raises(ValueError):
        terminal_route("urgent", has_dry_run=True)
