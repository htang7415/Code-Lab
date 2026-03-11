# Typing For Large Python Codebases

> Track: `software-engineering` | Topic: `python`

## Concept

Typing helps large Python codebases by making public boundaries explicit and by showing where interface drift would otherwise stay hidden until runtime.

## Key Points

- Missing annotations at public boundaries create ambiguity that spreads through the codebase.
- Return types matter as much as parameter types for readers and checkers.
- Protocol-style interfaces become useful when multiple implementations need one contract.

## Minimal Code Mental Model

```python
missing = missing_annotations({"user_id": "str", "limit": None}, return_type="list[str]")
ready = typed_api_ready({"user_id": "str", "limit": "int"}, return_type="list[str]")
protocol = needs_protocol(interface_methods=4, multiple_implementations=True)
```

## Function

```python
def missing_annotations(params: dict[str, str | None], return_type: str | None) -> list[str]:
def typed_api_ready(params: dict[str, str | None], return_type: str | None) -> bool:
def needs_protocol(interface_methods: int, multiple_implementations: bool) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/python/typing-for-large-python-codebases/python -q
```
