from __future__ import annotations


def select_tool(intent: str, tool_keywords: dict[str, list[str]]) -> str | None:
    intent_lower = intent.strip().lower()
    if not intent_lower:
        return None

    best_tool: str | None = None
    best_score = 0
    for tool_name, keywords in tool_keywords.items():
        score = sum(keyword.lower() in intent_lower for keyword in keywords)
        if score > best_score:
            best_tool = tool_name
            best_score = score
    return best_tool


def tool_call(name: str, arguments: dict[str, object], call_id: str = "call_1") -> dict[str, object]:
    if not name.strip():
        raise ValueError("name must be non-empty")
    if not call_id.strip():
        raise ValueError("call_id must be non-empty")
    return {
        "type": "tool_call",
        "id": call_id,
        "name": name,
        "arguments": arguments,
    }


def tool_result(call_id: str, output: object, is_error: bool = False) -> dict[str, object]:
    if not call_id.strip():
        raise ValueError("call_id must be non-empty")
    return {
        "type": "tool_result",
        "call_id": call_id,
        "output": output,
        "is_error": is_error,
    }
