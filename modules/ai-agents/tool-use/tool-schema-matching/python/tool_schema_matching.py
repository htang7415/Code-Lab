from __future__ import annotations


def schema_fields(schema: dict[str, object]) -> list[str]:
    properties = schema.get("properties", {})
    if not isinstance(properties, dict):
        return []
    fields: list[str] = []
    for key in properties:
        cleaned = str(key).strip()
        if cleaned:
            fields.append(cleaned)
    return fields


def schema_match_score(argument_names: list[str], field_names: list[str]) -> int:
    wanted = {name.strip() for name in argument_names if name.strip()}
    available = {name.strip() for name in field_names if name.strip()}
    return len(wanted & available)


def best_schema_match(argument_names: list[str], tool_schemas: dict[str, dict[str, object]]) -> str | None:
    best_tool: str | None = None
    best_score = 0
    for tool_name, schema in tool_schemas.items():
        score = schema_match_score(argument_names, schema_fields(schema))
        if score > best_score:
            best_tool = tool_name
            best_score = score
    return best_tool
