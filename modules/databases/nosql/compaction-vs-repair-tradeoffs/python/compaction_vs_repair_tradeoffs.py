"""compaction_vs_repair_tradeoffs - compaction fixes local read cost while repair fixes replica divergence."""

from __future__ import annotations


def validate_level_sstables(level_sstables: list[int]) -> None:
    if any(count < 0 for count in level_sstables):
        raise ValueError("level_sstables counts must be non-negative")


def validate_tradeoff_inputs(divergent_key_count: int, read_amp_threshold: int) -> None:
    if divergent_key_count < 0:
        raise ValueError("divergent_key_count must be non-negative")
    if read_amp_threshold <= 0:
        raise ValueError("read_amp_threshold must be positive")


def read_amplification(level_sstables: list[int]) -> int:
    validate_level_sstables(level_sstables)
    return sum(level_sstables)


def compacted_levels(level_sstables: list[int]) -> list[int]:
    validate_level_sstables(level_sstables)
    return [1 if count > 0 else 0 for count in level_sstables]


def repair_needed(divergent_key_count: int) -> bool:
    if divergent_key_count < 0:
        raise ValueError("divergent_key_count must be non-negative")
    return divergent_key_count > 0


def recommended_action(
    level_sstables: list[int],
    divergent_key_count: int,
    read_amp_threshold: int = 10,
) -> str:
    validate_tradeoff_inputs(divergent_key_count, read_amp_threshold)
    needs_compaction = read_amplification(level_sstables) >= read_amp_threshold
    needs_repair = repair_needed(divergent_key_count)
    if needs_compaction and needs_repair:
        return "both"
    if needs_compaction:
        return "compaction"
    if needs_repair:
        return "repair"
    return "neither"


def tradeoff_summary(
    level_sstables: list[int],
    divergent_key_count: int,
    read_amp_threshold: int = 10,
) -> dict[str, object]:
    validate_tradeoff_inputs(divergent_key_count, read_amp_threshold)
    before = read_amplification(level_sstables)
    after_levels = compacted_levels(level_sstables)
    after = read_amplification(after_levels)
    return {
        "read_amp_before": before,
        "read_amp_after_compaction": after,
        "divergent_key_count": divergent_key_count,
        "repair_needed": repair_needed(divergent_key_count),
        "recommended_action": recommended_action(
            level_sstables,
            divergent_key_count,
            read_amp_threshold,
        ),
    }
