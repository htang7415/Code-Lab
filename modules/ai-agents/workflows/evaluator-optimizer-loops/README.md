# Evaluator Optimizer Loops

> Track: `ai-agents` | Topic: `workflows`

## Concept

Evaluator-optimizer loops generate a draft, critique it against explicit checks, and send only the targeted feedback into the next revision step.

## Key Points

- This pattern is for improving a draft, not for repeating the same failed action blindly.
- The evaluator should return structured pass/fail checks plus concise feedback.
- The optimizer should stop after a bounded number of revisions and escalate if quality still misses the bar.

## Minimal Code Mental Model

```python
report = evaluation_report({"citations": True, "clarity": False})
route = optimizer_route(report["passed"], attempt=1, max_attempts=3)
packet = revision_packet("Draft answer", report["failed_checks"])
```

## Function

```python
def evaluation_report(check_results: dict[str, bool]) -> dict[str, object]:
def optimizer_route(passed: bool, attempt: int, max_attempts: int) -> str:
def revision_packet(draft: str, failed_checks: list[str]) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/ai-agents/workflows/evaluator-optimizer-loops/python -q
```
