# Prompt Chaining

> Track: `ai-agents` | Topic: `workflows`

## Concept

Prompt chaining breaks a larger task into ordered prompt stages where each stage passes a compact output to the next one.

## Key Points

- Chaining is useful when each stage has a clear transformation job.
- Stage outputs should stay compact so later prompts do not inherit the whole transcript.
- A failed stage should stop the chain instead of letting downstream prompts guess.

## Minimal Code Mental Model

```python
stages = chain_stages(["extract facts", "write summary", "check format"])
message = chained_prompt("facts: revenue up 12%", "write summary")
route = chain_route(stage_index=1, total_stages=3, previous_success=True)
```

## Function

```python
def chain_stages(stages: list[str]) -> list[dict[str, object]]:
def chained_prompt(previous_output: str, stage_instruction: str) -> str:
def chain_route(stage_index: int, total_stages: int, previous_success: bool) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/workflows/prompt-chaining/python -q
```
