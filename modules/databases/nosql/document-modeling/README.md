# Document Modeling

> Track: `databases` | Topic: `nosql`

## Concept

Document modeling keeps related nested data together when the natural read path wants the whole object in one fetch.

## Key Points

- Document shape is useful when nested data is usually read together.
- Appending nested items is simple when the aggregate is already one product object.
- You still need conventions for order, metadata, and schema evolution.
- Document models are a good fit for conversation state, configs, or session blobs with limited cross-document joins.

## Minimal Code Mental Model

```python
session = create_conversation_document("sess-1", 42)
append_message(session, "user", "Find failed runs", "2026-03-11T10:00:00Z")
append_message(session, "assistant", "I found three failed runs.", "2026-03-11T10:00:02Z")
reply = latest_message_by_role(session, "assistant")
```

## Function

```python
def create_conversation_document(session_id: str, user_id: int) -> dict[str, object]:
def append_message(
    document: dict[str, object],
    role: str,
    text: str,
    created_at: str,
    metadata: dict[str, object] | None = None,
) -> None:
def latest_message_by_role(
    document: dict[str, object],
    role: str,
) -> dict[str, object] | None:
def conversation_summary(document: dict[str, object]) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/nosql/document-modeling/python -q
```
