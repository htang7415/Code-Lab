from __future__ import annotations


def done_indicator_batch(done_flags: list[bool]) -> list[float]:
    return [1.0 if done else 0.0 for done in done_flags]
