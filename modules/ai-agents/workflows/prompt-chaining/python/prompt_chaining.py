from __future__ import annotations


def chain_stages(stages: list[str]) -> list[dict[str, object]]:
    if not stages:
        raise ValueError("stages must be non-empty")

    packets: list[dict[str, object]] = []
    for index, stage in enumerate(stages):
        cleaned_stage = stage.strip()
        if not cleaned_stage:
            raise ValueError("stage names must be non-empty")
        packets.append(
            {
                "stage_index": index,
                "instruction": cleaned_stage,
                "is_last": index == len(stages) - 1,
            }
        )
    return packets


def chained_prompt(previous_output: str, stage_instruction: str) -> str:
    cleaned_output = previous_output.strip()
    cleaned_instruction = stage_instruction.strip()
    if not cleaned_output:
        raise ValueError("previous_output must be non-empty")
    if not cleaned_instruction:
        raise ValueError("stage_instruction must be non-empty")
    return f"Previous stage output:\n{cleaned_output}\n\nNext stage:\n{cleaned_instruction}"


def chain_route(stage_index: int, total_stages: int, previous_success: bool) -> str:
    if stage_index < 0:
        raise ValueError("stage_index must be non-negative")
    if total_stages <= 0:
        raise ValueError("total_stages must be positive")
    if stage_index >= total_stages:
        raise ValueError("stage_index must be smaller than total_stages")
    if not previous_success:
        return "stop"
    if stage_index == total_stages - 1:
        return "complete"
    return "next-stage"
