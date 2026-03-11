from __future__ import annotations


TRANSITIONS = {
    "draft": {"approved", "cancelled"},
    "approved": {"fulfilling", "cancelled"},
    "fulfilling": {"shipped"},
    "shipped": set(),
    "cancelled": set(),
}

TERMINAL_STATES = {"shipped", "cancelled"}


def can_transition(current: str, nxt: str) -> bool:
    return nxt in TRANSITIONS.get(current, set())


def apply_transition(current: str, nxt: str) -> str:
    if not can_transition(current, nxt):
        raise ValueError(f"invalid transition: {current} -> {nxt}")
    return nxt


def terminal_state(state: str) -> bool:
    return state in TERMINAL_STATES
