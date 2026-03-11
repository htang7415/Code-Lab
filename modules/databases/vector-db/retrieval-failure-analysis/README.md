# Retrieval Failure Analysis

> Track: `databases` | Topic: `vector-db`

## Concept

When retrieval quality is bad, the first useful question is what kind of failure happened: scope leak, no relevant hit, or relevant results ranked too low.

## Key Points

- A wrong-tenant result is a correctness failure, not just a ranking issue.
- If no relevant result appears anywhere, recall is the main problem.
- If relevant results exist but appear below `k`, ranking is the main problem.
- Failure labels make debugging retrieval systems more systematic than looking at one score.

## Minimal Code Mental Model

```python
results = [
    {"id": "a", "workspace_id": 8},
    {"id": "b", "workspace_id": 7},
]
reason = failure_reason(results, relevant_ids={"b"}, allowed_workspace_id=7, k=1)
```

## Function

```python
def first_relevant_rank(
    ranked_ids: list[str],
    relevant_ids: set[str],
) -> int | None:
def has_scope_leak(
    ranked_results: list[dict[str, object]],
    allowed_workspace_id: int,
    k: int,
) -> bool:
def failure_reason(
    ranked_results: list[dict[str, object]],
    relevant_ids: set[str],
    allowed_workspace_id: int,
    k: int,
) -> str:
def failure_summary(
    cases: list[dict[str, object]],
    k: int,
) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/databases/vector-db/retrieval-failure-analysis/python -q
```
