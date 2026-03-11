# Tool Schema Matching

> Track: `ai-agents` | Topic: `tool-use`

## Concept

Tool schema matching compares the arguments a user seems to need with the fields a tool actually accepts.

## Key Points

- Matching should happen before the tool call so the agent picks a compatible tool.
- Simple field overlap is often enough for a first routing pass.
- Explicit schema inspection is easier to debug than implicit prompt-only matching.

## Minimal Code Mental Model

```python
fields = schema_fields({"properties": {"city": {}, "units": {}}})
score = schema_match_score(["city", "units"], fields)
tool = best_schema_match(["city"], {"weather": {"properties": {"city": {}, "units": {}}}})
```

## Function

```python
def schema_fields(schema: dict[str, object]) -> list[str]:
def schema_match_score(argument_names: list[str], field_names: list[str]) -> int:
def best_schema_match(argument_names: list[str], tool_schemas: dict[str, dict[str, object]]) -> str | None:
```

## Run tests

```bash
pytest modules/ai-agents/tool-use/tool-schema-matching/python -q
```
