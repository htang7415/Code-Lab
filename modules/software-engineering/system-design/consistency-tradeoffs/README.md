# Consistency Tradeoffs

> Track: `software-engineering` | Topic: `system-design`

## Concept

Consistency choices decide whether a system optimizes for immediate correctness across replicas and components or accepts temporary divergence for availability and latency.

## Key Points

- Strong consistency is most valuable when cross-entity invariants matter.
- Eventual consistency is easier to scale when stale reads are acceptable.
- Write conflicts and stale-read tolerance are the main design signals.

## Minimal Code Mental Model

```python
mode = consistency_mode(cross_entity_invariant=True, stale_reads_tolerable=False)
risk = read_write_conflict_risk(concurrent_writers=4, stale_reads_tolerable=False)
decision = consistency_decision(cross_entity_invariant=False, stale_reads_tolerable=True, concurrent_writers=1)
```

## Function

```python
def consistency_mode(cross_entity_invariant: bool, stale_reads_tolerable: bool) -> str:
def read_write_conflict_risk(concurrent_writers: int, stale_reads_tolerable: bool) -> str:
def consistency_decision(
    cross_entity_invariant: bool,
    stale_reads_tolerable: bool,
    concurrent_writers: int,
) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/system-design/consistency-tradeoffs/python -q
```
