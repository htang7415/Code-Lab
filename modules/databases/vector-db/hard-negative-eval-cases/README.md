# Hard Negative Eval Cases

> Track: `databases` | Topic: `vector-db`

## Concept

Hard negatives are distractors that look plausible to the retriever but are still wrong. A retrieval eval set without them can overestimate quality because the ranking problem is too easy.

## Key Points

- Easy negatives measure filtering; hard negatives measure ranking quality.
- Each case should pair one known positive with one or more confusing wrong candidates.
- Hard-negative coverage matters for AI agents because near-duplicate docs and stale memories are common failure modes.
- If the positive appears inside the negative set, the case is malformed and the metric signal gets muddy.

## Minimal Code Mental Model

```python
cases = [
    hard_negative_case("q1", "doc-1", ["doc-2", "doc-3"], "semantic"),
    hard_negative_case("q2", "doc-9", ["doc-8"], "keyword"),
]
summary = dataset_summary(cases)
```

## Function

```python
def hard_negative_case(
    query_id: str,
    positive_id: str,
    hard_negative_ids: list[str],
    query_type: str,
) -> dict[str, object]:
def hard_negative_count(cases: list[dict[str, object]]) -> int:
def invalid_case_ids(cases: list[dict[str, object]]) -> list[str]:
def query_type_counts(cases: list[dict[str, object]]) -> dict[str, int]:
def dataset_summary(cases: list[dict[str, object]]) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/vector-db/hard-negative-eval-cases/python -q
```
