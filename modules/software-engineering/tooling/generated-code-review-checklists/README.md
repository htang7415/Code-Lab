# Generated Code Review Checklists

> Track: `software-engineering` | Topic: `tooling`

## Concept

Generated code should pass an explicit review checklist so reviewers verify the right risks instead of reacting to whatever the diff happens to highlight.

## Key Points

- Review quality drops when the checklist lives only in reviewer memory.
- Different change types need different blocking questions.
- Merge should depend on completed review items, not reviewer confidence alone.

## Minimal Code Mental Model

```python
required = review_checklist(["api", "security", "ai-generated"])
blockers = missing_review_items(required, completed)
ready = review_complete(required, completed)
```

## Function

```python
def review_checklist(change_tags: list[str]) -> list[str]:
def missing_review_items(required_items: list[str], completed_items: dict[str, bool]) -> list[str]:
def review_complete(required_items: list[str], completed_items: dict[str, bool]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/tooling/generated-code-review-checklists/python -q
```
