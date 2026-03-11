# Context Engineering for Agents

> Track: `ai-agents` | Topic: `prompting`

## Concept

Context engineering for agents decides which instructions, memory, and retrieved evidence should fit into the active prompt before the model generates anything.

## Key Points

- The active prompt is a packed working set, not the full system history.
- Context blocks should be ranked before packing so low-value text drops first.
- Output space must be reserved before prompt packing begins.

## Minimal Code Mental Model

```python
budget = available_context_budget(context_window=8192, reserved_output_tokens=1024)
ranked = rank_context_blocks(blocks)
packed = pack_context_blocks(ranked, token_budget=budget)
```

## Function

```python
def available_context_budget(context_window: int, reserved_output_tokens: int) -> int:
def rank_context_blocks(blocks: list[dict[str, object]]) -> list[dict[str, object]]:
def pack_context_blocks(blocks: list[dict[str, object]], token_budget: int) -> list[str]:
```

## Run tests

```bash
pytest modules/ai-agents/prompting/context-engineering-for-agents/python -q
```
