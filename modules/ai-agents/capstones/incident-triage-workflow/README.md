# Incident Triage Workflow

> Track: `ai-agents` | Topic: `capstones`

## Concept

This capstone combines route scoring, bounded retries, latency budgeting, escalation, and trace-friendly workflow state into one compact incident-triage loop.

## Key Points

- Route choice should be explicit instead of hidden in prompt wording.
- Retries and latency budgets should be bounded before the workflow starts.
- Escalation should happen for a named reason, not as a generic failure bucket.
- The workflow should emit enough structured state that operators can see what happened.

## Core Math

- Route score margin:
  $$
  \text{best route score} - \text{runner-up score}
  $$
- Remaining latency:
  $$
  \text{total budget} - \text{elapsed} - \text{reserved response}
  $$
- Escalation rule:
  $$
  \text{blocked} \;\lor\; \text{confidence} < \tau \;\lor\; \text{attempt} \ge \text{max attempts}
  $$

## Minimal Code Mental Model

```python
route = select_incident_route(route_scores, min_score=0.6, min_margin=0.1)
remaining = remaining_latency_budget(total_budget_ms=1200, elapsed_ms=300, reserved_response_ms=150)
decision = incident_triage_workflow(
    route_scores,
    blocked=False,
    confidence=0.86,
    attempt=1,
    max_attempts=2,
    total_budget_ms=1200,
    elapsed_ms=300,
    required_step_budget_ms=250,
)
```

## Function

```python
def select_incident_route(
    route_scores: dict[str, float],
    min_score: float,
    min_margin: float = 0.0,
) -> str:
def remaining_latency_budget(
    total_budget_ms: int,
    elapsed_ms: int,
    reserved_response_ms: int = 0,
) -> int:
def incident_escalation_reason(
    blocked: bool,
    confidence: float,
    min_confidence: float,
    attempt: int,
    max_attempts: int,
    remaining_budget_ms: int,
    required_step_budget_ms: int,
) -> str | None:
def triage_trace_packet(
    route: str,
    action: str,
    reason: str | None,
    remaining_budget_ms: int,
) -> dict[str, object]:
def incident_triage_workflow(
    route_scores: dict[str, float],
    blocked: bool,
    confidence: float,
    attempt: int,
    max_attempts: int,
    total_budget_ms: int,
    elapsed_ms: int,
    required_step_budget_ms: int,
    min_route_score: float = 0.6,
    min_route_margin: float = 0.1,
    min_confidence: float = 0.7,
    reserved_response_ms: int = 0,
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/ai-agents/capstones/incident-triage-workflow/python -q
```
