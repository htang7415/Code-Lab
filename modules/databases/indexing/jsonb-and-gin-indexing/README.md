# JSONB And GIN Indexing

> Track: `databases` | Topic: `indexing`

## Concept

GIN-style indexing is an inverted index mental model: instead of ordering rows by one key, it maps many JSONB or array terms back to the rows that contain them.

## Key Points

- JSONB fields can hold flexible metadata without breaking the relational model.
- Inverted indexes are useful when queries search for terms inside nested or repeated metadata.
- Multi-term filters become set intersections over postings lists.
- Updating indexed JSON metadata means removing old terms and adding new ones.

## Minimal Code Mental Model

```python
documents = [
    {"id": "doc-1", "metadata": {"language": "en", "tags": ["rag", "eval"]}},
]
inverted = build_metadata_inverted_index(documents)
matches = filter_documents_with_index(inverted, ["language=en", "tag=rag"])
```

## Function

```python
def metadata_terms(document: dict[str, object]) -> set[str]:
def build_metadata_inverted_index(
    documents: list[dict[str, object]],
) -> dict[str, set[str]]:
def filter_documents_with_index(
    inverted_index: dict[str, set[str]],
    required_terms: list[str],
) -> list[str]:
def update_term_diff(
    previous_document: dict[str, object],
    new_document: dict[str, object],
) -> tuple[set[str], set[str]]:
```

## Run tests

```bash
pytest modules/databases/indexing/jsonb-and-gin-indexing/python -q
```
