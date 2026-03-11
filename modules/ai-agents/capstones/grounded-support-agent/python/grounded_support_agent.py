from __future__ import annotations


def build_support_context(
    retrieved_chunks: list[tuple[str, float]],
    memories: list[str],
    max_chunks: int = 2,
    max_memories: int = 1,
) -> dict[str, list[str]]:
    if max_chunks <= 0:
        raise ValueError("max_chunks must be positive")
    if max_memories < 0:
        raise ValueError("max_memories must be non-negative")

    ranked_chunks: list[tuple[str, float]] = []
    for text, score in retrieved_chunks:
        cleaned_text = str(text).strip()
        if not cleaned_text:
            continue
        if score < 0.0:
            raise ValueError("retrieval scores must be non-negative")
        ranked_chunks.append((cleaned_text, float(score)))

    selected_retrieved = [
        text
        for text, _ in sorted(
            ranked_chunks,
            key=lambda item: (-item[1], item[0]),
        )[:max_chunks]
    ]
    cleaned_memories = [memory.strip() for memory in memories if memory.strip()]
    selected_memories = cleaned_memories[-max_memories:] if max_memories else []

    return {
        "retrieved": selected_retrieved,
        "memories": selected_memories,
        "context_blocks": selected_retrieved + selected_memories,
    }


def expected_tool_value(
    success_probability: float,
    success_value: float,
    tool_cost: float,
    failure_penalty: float = 0.0,
) -> float:
    if not 0.0 <= success_probability <= 1.0:
        raise ValueError("success_probability must satisfy 0 <= value <= 1")
    if success_value < 0.0:
        raise ValueError("success_value must be non-negative")
    if tool_cost < 0.0:
        raise ValueError("tool_cost must be non-negative")
    if failure_penalty < 0.0:
        raise ValueError("failure_penalty must be non-negative")
    return success_probability * success_value - tool_cost - (1.0 - success_probability) * failure_penalty


def select_support_tool(
    tool_to_profile: dict[str, dict[str, float]],
    min_expected_value: float,
    min_margin: float = 0.0,
) -> str:
    if min_margin < 0.0:
        raise ValueError("min_margin must be non-negative")
    if not tool_to_profile:
        return "skip"

    ranked: list[dict[str, object]] = []
    for tool_name, profile in tool_to_profile.items():
        cleaned_name = tool_name.strip()
        if not cleaned_name:
            raise ValueError("tool names must be non-empty")
        ranked.append(
            {
                "tool": cleaned_name,
                "expected_value": expected_tool_value(
                    success_probability=float(profile.get("success_probability", 0.0)),
                    success_value=float(profile.get("success_value", 0.0)),
                    tool_cost=float(profile.get("tool_cost", 0.0)),
                    failure_penalty=float(profile.get("failure_penalty", 0.0)),
                ),
            }
        )

    ranked.sort(key=lambda item: (-float(item["expected_value"]), str(item["tool"])))
    top_value = float(ranked[0]["expected_value"])
    if top_value < min_expected_value:
        return "skip"

    second_value = float(ranked[1]["expected_value"]) if len(ranked) > 1 else float("-inf")
    if second_value != float("-inf") and top_value - second_value < min_margin:
        return "review"
    return str(ranked[0]["tool"])


def grounded_support_decision(
    retrieved_chunks: list[tuple[str, float]],
    memories: list[str],
    tool_to_profile: dict[str, dict[str, float]],
    blocked: bool,
    confidence: float,
    grounding_coverage: float,
    min_confidence: float = 0.7,
    min_grounding: float = 0.75,
    min_expected_value: float = 0.0,
    min_margin: float = 0.0,
    max_chunks: int = 2,
    max_memories: int = 1,
) -> dict[str, object]:
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must satisfy 0 <= value <= 1")
    if not 0.0 <= grounding_coverage <= 1.0:
        raise ValueError("grounding_coverage must satisfy 0 <= value <= 1")
    if not 0.0 <= min_confidence <= 1.0:
        raise ValueError("min_confidence must satisfy 0 <= value <= 1")
    if not 0.0 <= min_grounding <= 1.0:
        raise ValueError("min_grounding must satisfy 0 <= value <= 1")

    context = build_support_context(
        retrieved_chunks,
        memories,
        max_chunks=max_chunks,
        max_memories=max_memories,
    )

    if blocked:
        route = "block"
    elif confidence < min_confidence or grounding_coverage < min_grounding:
        route = "review"
    else:
        tool_route = select_support_tool(
            tool_to_profile,
            min_expected_value=min_expected_value,
            min_margin=min_margin,
        )
        if tool_route == "review":
            route = "review"
        elif tool_route == "skip":
            route = "answer-from-context"
        else:
            route = f"tool:{tool_route}"

    return {
        "route": route,
        "context": context,
        "confidence": confidence,
        "grounding_coverage": grounding_coverage,
    }
