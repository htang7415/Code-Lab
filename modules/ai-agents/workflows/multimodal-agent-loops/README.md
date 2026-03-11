# Multimodal Agent Loops

> Track: `ai-agents` | Topic: `workflows`

## Concept

Multimodal agent loops decide whether the workflow has the required text, image, audio, or video inputs, whether tools should run over them, and when the system should answer, ask for more input, or escalate.

## Key Points

- Multimodal workflows fail early when required modalities are missing.
- Tool use over modalities should be explicit, not assumed from the final answer step.
- This workflow layer builds on the model-side multimodal modules by routing execution around modality availability.

## Minimal Code Mental Model

```python
missing = missing_modalities(["text", "image"], ["text"])
packet = multimodal_task_packet("caption image and verify logo", ["text", "image"], ["vision_parse"])
route = multimodal_execution_route(missing, packet["tool_plan"])
```

## Function

```python
def missing_modalities(required_modalities: list[str], available_modalities: list[str]) -> list[str]:
def multimodal_task_packet(
    task: str,
    required_modalities: list[str],
    tool_plan: list[str] | None = None,
) -> dict[str, object]:
def multimodal_execution_route(missing: list[str], tool_plan: list[str]) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/workflows/multimodal-agent-loops/python -q
```
