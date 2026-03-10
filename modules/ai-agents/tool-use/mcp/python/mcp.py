from __future__ import annotations


def server_capabilities(
    tool_count: int = 0,
    resource_count: int = 0,
    prompt_count: int = 0,
) -> dict[str, bool]:
    counts = [tool_count, resource_count, prompt_count]
    if any(count < 0 for count in counts):
        raise ValueError("counts must be non-negative")
    return {
        "tools": tool_count > 0,
        "resources": resource_count > 0,
        "prompts": prompt_count > 0,
    }


def tool_descriptor(name: str, description: str) -> dict[str, str]:
    if not name.strip():
        raise ValueError("name must be non-empty")
    if not description.strip():
        raise ValueError("description must be non-empty")
    return {"name": name, "description": description}


def tool_call_request(name: str, arguments: dict[str, object]) -> dict[str, object]:
    if not name.strip():
        raise ValueError("name must be non-empty")
    return {
        "method": "tools/call",
        "params": {
            "name": name,
            "arguments": arguments,
        },
    }
