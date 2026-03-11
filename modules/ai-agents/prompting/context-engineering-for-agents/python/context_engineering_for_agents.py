from __future__ import annotations


def available_context_budget(context_window: int, reserved_output_tokens: int) -> int:
    if context_window <= 0:
        raise ValueError("context_window must be positive")
    if reserved_output_tokens < 0:
        raise ValueError("reserved_output_tokens must be non-negative")
    if reserved_output_tokens >= context_window:
        raise ValueError("reserved_output_tokens must be smaller than context_window")
    return context_window - reserved_output_tokens


def rank_context_blocks(blocks: list[dict[str, object]]) -> list[dict[str, object]]:
    if not blocks:
        raise ValueError("blocks must be non-empty")

    ranked: list[dict[str, object]] = []
    for block in blocks:
        name = str(block.get("name", "")).strip()
        tokens = int(block.get("tokens", 0))
        priority = int(block.get("priority", 0))
        if not name:
            raise ValueError("block names must be non-empty")
        if tokens <= 0:
            raise ValueError("block tokens must be positive")
        ranked.append({"name": name, "tokens": tokens, "priority": priority})

    return sorted(ranked, key=lambda block: (-int(block["priority"]), int(block["tokens"]), str(block["name"])))


def pack_context_blocks(blocks: list[dict[str, object]], token_budget: int) -> list[str]:
    if token_budget <= 0:
        raise ValueError("token_budget must be positive")

    packed: list[str] = []
    remaining = token_budget
    for block in blocks:
        tokens = int(block.get("tokens", 0))
        name = str(block.get("name", "")).strip()
        if not name:
            raise ValueError("block names must be non-empty")
        if tokens <= 0:
            raise ValueError("block tokens must be positive")
        if tokens <= remaining:
            packed.append(name)
            remaining -= tokens
    return packed
