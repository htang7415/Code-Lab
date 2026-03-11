# Compaction Vs Repair Tradeoffs

> Track: `databases` | Topic: `nosql`

## Concept

Compaction and repair are not substitutes. Compaction reduces read amplification and storage fragmentation, while repair fixes replica divergence.

## Key Points

- Compaction is a local storage optimization.
- Repair is a replica-consistency operation.
- High read amplification points toward compaction.
- Divergent replicas point toward repair, even if read amplification is fine.
- SSTable counts and divergent-key counts should be non-negative, and the read-amplification threshold should stay positive.

## Minimal Code Mental Model

```python
summary = tradeoff_summary(
    level_sstables=[3, 5, 10],
    divergent_key_count=2,
)
```

## Function

```python
def validate_level_sstables(level_sstables: list[int]) -> None:
def validate_tradeoff_inputs(divergent_key_count: int, read_amp_threshold: int) -> None:
def read_amplification(level_sstables: list[int]) -> int:
def compacted_levels(level_sstables: list[int]) -> list[int]:
def repair_needed(divergent_key_count: int) -> bool:
def recommended_action(
    level_sstables: list[int],
    divergent_key_count: int,
    read_amp_threshold: int = 10,
) -> str:
def tradeoff_summary(
    level_sstables: list[int],
    divergent_key_count: int,
    read_amp_threshold: int = 10,
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/nosql/compaction-vs-repair-tradeoffs/python -q
```
