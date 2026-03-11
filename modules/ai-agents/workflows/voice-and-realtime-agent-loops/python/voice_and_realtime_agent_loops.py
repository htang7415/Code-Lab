from __future__ import annotations


def voice_turn_packet(
    input_mode: str,
    transcript: str | None = None,
    interrupted: bool = False,
) -> dict[str, object]:
    cleaned_mode = input_mode.strip().lower()
    if cleaned_mode not in {"audio", "text", "multimodal"}:
        raise ValueError("input_mode must be audio, text, or multimodal")

    cleaned_transcript = transcript.strip() if transcript is not None else None
    if cleaned_mode == "audio" and not cleaned_transcript and not interrupted:
        raise ValueError("audio turns need a transcript unless interrupted")

    return {
        "input_mode": cleaned_mode,
        "transcript": cleaned_transcript,
        "interrupted": interrupted,
    }


def realtime_budget_ok(latency_ms: int, max_latency_ms: int) -> bool:
    if latency_ms < 0:
        raise ValueError("latency_ms must be non-negative")
    if max_latency_ms <= 0:
        raise ValueError("max_latency_ms must be positive")
    return latency_ms <= max_latency_ms


def realtime_route(has_transcript: bool, interrupted: bool, needs_tool: bool) -> str:
    if interrupted:
        return "yield"
    if not has_transcript:
        return "wait"
    if needs_tool:
        return "run-tool"
    return "respond"
