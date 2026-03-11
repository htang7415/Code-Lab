# Cache Key Design

> Track: `databases` | Topic: `caching`

## Concept

Good cache keys encode the scope and version that make a value safe to reuse. Bad keys silently collide across tenants, variants, or model versions.

## Key Points

- Keys should include tenant or workspace scope when data is tenant-specific.
- Keys should include version or model identity when behavior changes across releases.
- Optional parameters should be normalized so logically identical requests map to the same key.
- A short key is useless if it aliases two different values.
- Key parts should avoid reserved delimiters like `|` and `=` or parsing becomes ambiguous.

## Minimal Code Mental Model

```python
key = cache_key(
    namespace="answer",
    workspace_id=7,
    resource_id="doc-42",
    version="v2",
    extras={"lang": "en", "mode": "summary"},
)
parts = parse_cache_key(key)
```

## Function

```python
def validate_key_fragment(name: str, value: str) -> None:
def cache_key(
    namespace: str,
    workspace_id: int,
    resource_id: str,
    version: str,
    extras: dict[str, object] | None = None,
) -> str:
def parse_cache_key(key: str) -> dict[str, object]:
def naive_key(resource_id: str) -> str:
def key_collides(left: str, right: str) -> bool:
```

## Run tests

```bash
pytest modules/databases/caching/cache-key-design/python -q
```
