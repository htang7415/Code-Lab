from __future__ import annotations


def missing_modalities(required_modalities: list[str], available_modalities: list[str]) -> list[str]:
    required = {modality.strip().lower() for modality in required_modalities if modality.strip()}
    available = {modality.strip().lower() for modality in available_modalities if modality.strip()}
    if not required:
        raise ValueError("required_modalities must be non-empty")
    return sorted(required - available)


def multimodal_task_packet(
    task: str,
    required_modalities: list[str],
    tool_plan: list[str] | None = None,
) -> dict[str, object]:
    cleaned_task = task.strip()
    if not cleaned_task:
        raise ValueError("task must be non-empty")

    cleaned_required = [modality.strip().lower() for modality in required_modalities if modality.strip()]
    if not cleaned_required:
        raise ValueError("required_modalities must be non-empty")

    cleaned_tools = []
    for tool in tool_plan or []:
        cleaned_tool = tool.strip()
        if cleaned_tool:
            cleaned_tools.append(cleaned_tool)

    return {
        "task": cleaned_task,
        "required_modalities": cleaned_required,
        "tool_plan": cleaned_tools,
    }


def multimodal_execution_route(missing: list[str], tool_plan: list[str]) -> str:
    if missing:
        return "request-modalities"
    if tool_plan:
        return "run-tools"
    return "answer"
