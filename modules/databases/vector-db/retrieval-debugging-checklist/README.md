# Retrieval Debugging Checklist

> Track: `databases` | Topic: `vector-db`

## Concept

When retrieval fails, the fastest path is a short checklist tied to the failure mode instead of random tuning.

## Key Points

- Scope leaks usually point to metadata filtering or access-control bugs.
- No relevant hit usually points to chunking, embedding coverage, or indexing gaps.
- Relevant hits below `k` usually point to ranking, hybrid weights, or reranking problems.
- A checklist makes debugging systematic and easier to hand off across a team.

## Minimal Code Mental Model

```python
steps = checklist_for_failure("ranked-below-k")
report = checklist_report(
    [
        {"query_id": "q1", "failure": "scope-leak"},
        {"query_id": "q2", "failure": "ranked-below-k"},
    ]
)
```

## Function

```python
def checklist_for_failure(failure: str) -> list[str]:
def first_step(failure: str) -> str:
def checklist_report(cases: list[dict[str, str]]) -> dict[str, list[str]]:
```

## Run tests

```bash
pytest modules/databases/vector-db/retrieval-debugging-checklist/python -q
```
