# Storage Choice Basics

> Track: `software-engineering` | Topic: `system-design`

## Concept

Storage choice should follow the access pattern and correctness requirements instead of defaulting every workload to the same database.

## Key Points

- Transaction-heavy source-of-truth data usually belongs in a relational store.
- Search and vector retrieval are access patterns, not replacements for core transactional state.
- Multiple requirements often justify a hybrid design rather than forcing one store to do everything.

## Minimal Code Mental Model

```python
store = primary_storage(needs_transactions=True, document_search=False, vector_similarity=False)
hybrid = hybrid_needed(needs_transactions=True, document_search=True, vector_similarity=False)
tradeoff = storage_tradeoff("vector")
```

## Function

```python
def primary_storage(needs_transactions: bool, document_search: bool, vector_similarity: bool) -> str:
def hybrid_needed(needs_transactions: bool, document_search: bool, vector_similarity: bool) -> bool:
def storage_tradeoff(storage: str) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/system-design/storage-choice-basics/python -q
```
