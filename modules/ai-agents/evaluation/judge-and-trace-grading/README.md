# Judge and Trace Grading

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Judge-and-trace grading combines a final-answer judge score with step-trace status so an agent run is not accepted just because the last answer sounds good.

## Key Points

- A strong final answer can still hide blocked or failed steps earlier in the trace.
- Judge scores are most useful when they are combined with execution evidence, not read alone.
- This pattern builds on judge-style evaluation by adding trace-aware routing for pass, review, or fail.

## Minimal Code Mental Model

```python
score = mean_judge_score([0.9, 0.8, 0.7])
packet = trace_grade_packet("run_7", score, ["done", "blocked", "done"])
route = judge_trace_route(packet["judge_score"], packet["blocked_or_failed_steps"], threshold=0.8)
```

## Function

```python
def mean_judge_score(scores: list[float]) -> float:
def trace_grade_packet(run_id: str, judge_score: float, step_statuses: list[str]) -> dict[str, object]:
def judge_trace_route(judge_score: float, blocked_or_failed_steps: int, threshold: float) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/judge-and-trace-grading/python -q
```
