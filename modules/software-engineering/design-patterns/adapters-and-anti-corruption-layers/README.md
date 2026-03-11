# Adapters And Anti-Corruption Layers

> Track: `software-engineering` | Topic: `design-patterns`

## Concept

Adapters translate externally owned data into a smaller internal contract so vendor naming and status quirks do not leak through the codebase.

## Key Points

- External schemas change for reasons your system does not control.
- Internal contracts should keep stable names and meanings.
- A boundary translator should drop fields that are not part of the internal model.

## Minimal Code Mental Model

```python
translated = translate_billing_event(
    {"event_id": "evt_1", "state": "paid", "amount": 4200, "currency": "usd"}
)
assert translated["status"] == "settled"
assert preserves_internal_contract(translated) is True
```

## Function

```python
def vendor_status_to_internal(status: str) -> str:
def translate_billing_event(event: dict[str, object]) -> dict[str, object]:
def preserves_internal_contract(event: dict[str, object]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/design-patterns/adapters-and-anti-corruption-layers/python -q
```
