"""compaction_debt_signals - combine backlog signals into a compaction recommendation."""

from __future__ import annotations


def validate_level_sstables(level_sstables: list[int]) -> None:
    if any(count < 0 for count in level_sstables):
        raise ValueError("level_sstables counts must be non-negative")


def validate_inputs(tombstone_ratio: float, pending_bytes_mb: int) -> None:
    if not 0.0 <= tombstone_ratio <= 1.0:
        raise ValueError("tombstone_ratio must be between 0 and 1")
    if pending_bytes_mb < 0:
        raise ValueError("pending_bytes_mb must be non-negative")


def read_amplification(level_sstables: list[int]) -> int:
    validate_level_sstables(level_sstables)
    return sum(level_sstables)


def debt_signals(
    level_sstables: list[int],
    tombstone_ratio: float,
    pending_bytes_mb: int,
) -> dict[str, bool]:
    validate_inputs(tombstone_ratio, pending_bytes_mb)
    return {
        "high_read_amp": read_amplification(level_sstables) >= 14,
        "high_tombstones": tombstone_ratio >= 0.2,
        "high_pending_bytes": pending_bytes_mb >= 512,
    }


def recommended_action(
    level_sstables: list[int],
    tombstone_ratio: float,
    pending_bytes_mb: int,
) -> str:
    signals = debt_signals(level_sstables, tombstone_ratio, pending_bytes_mb)
    signal_count = sum(1 for value in signals.values() if value)
    if signal_count >= 2:
        return "compact-now"
    if signal_count == 1:
        return "compact-soon"
    return "observe"


def compaction_summary(
    level_sstables: list[int],
    tombstone_ratio: float,
    pending_bytes_mb: int,
) -> dict[str, object]:
    validate_inputs(tombstone_ratio, pending_bytes_mb)
    signals = debt_signals(level_sstables, tombstone_ratio, pending_bytes_mb)
    return {
        "read_amplification": read_amplification(level_sstables),
        "tombstone_ratio": tombstone_ratio,
        "pending_bytes_mb": pending_bytes_mb,
        "signals": signals,
        "recommended_action": recommended_action(
            level_sstables,
            tombstone_ratio,
            pending_bytes_mb,
        ),
    }
