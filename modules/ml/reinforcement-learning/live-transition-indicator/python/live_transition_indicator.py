from __future__ import annotations


def live_transition_indicator(done: bool) -> float:
    return 0.0 if done else 1.0
