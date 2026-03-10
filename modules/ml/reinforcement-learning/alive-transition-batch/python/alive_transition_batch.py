from __future__ import annotations


def alive_transition_batch(done_flags: list[bool]) -> list[float]:
    return [0.0 if done else 1.0 for done in done_flags]
