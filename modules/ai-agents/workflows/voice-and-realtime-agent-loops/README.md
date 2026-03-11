# Voice and Realtime Agent Loops

> Track: `ai-agents` | Topic: `workflows`

## Concept

Voice and realtime agent loops route streaming turns by checking whether transcript state, interruption state, and latency budget still allow the agent to keep responding live.

## Key Points

- Realtime loops must react to interruption before they optimize response quality.
- Transcript availability and response latency are workflow constraints, not just model details.
- Voice workflows often need to choose between waiting, responding, or yielding control to a tool.

## Minimal Code Mental Model

```python
packet = voice_turn_packet("audio", transcript="schedule meeting tomorrow", interrupted=False)
within_budget = realtime_budget_ok(latency_ms=180, max_latency_ms=250)
route = realtime_route(has_transcript=True, interrupted=False, needs_tool=True)
```

## Function

```python
def voice_turn_packet(
    input_mode: str,
    transcript: str | None = None,
    interrupted: bool = False,
) -> dict[str, object]:
def realtime_budget_ok(latency_ms: int, max_latency_ms: int) -> bool:
def realtime_route(has_transcript: bool, interrupted: bool, needs_tool: bool) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/workflows/voice-and-realtime-agent-loops/python -q
```
