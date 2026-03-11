# Golden Query Eval Sets

> Track: `databases` | Topic: `vector-db`

## Concept

A golden query set is a small stable retrieval regression suite. It should cover the important query types and stay fixed enough that metric changes actually mean something.

## Key Points

- Golden sets are for regression tracking, not broad offline exploration.
- Each case should have a stable expected answer.
- Coverage matters: keyword, semantic, and multi-hop queries usually fail differently.
- Duplicate IDs or missing coverage weaken the regression signal.

## Minimal Code Mental Model

```python
cases = [
    golden_case("q1", "a", "keyword"),
    golden_case("q2", "b", "semantic"),
    golden_case("q3", "c", "multi-hop"),
]
summary = golden_set_summary(cases, required_types=["keyword", "semantic", "multi-hop"], min_case_count=3)
```

## Function

```python
def golden_case(query_id: str, expected_top_id: str, query_type: str) -> dict[str, str]:
def duplicate_query_ids(cases: list[dict[str, str]]) -> list[str]:
def missing_required_types(
    cases: list[dict[str, str]],
    required_types: list[str],
) -> list[str]:
def golden_set_ready(
    cases: list[dict[str, str]],
    required_types: list[str],
    min_case_count: int,
) -> bool:
def golden_set_summary(
    cases: list[dict[str, str]],
    required_types: list[str],
    min_case_count: int,
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/vector-db/golden-query-eval-sets/python -q
```
