# Capstones

This section is for end-to-end synthesis work after the main `ai-agents` foundations are in place.

## Purpose

Use this page to combine:
- prompt structure
- retrieval and memory
- tool choice
- routing and escalation
- observability, evaluation, and guardrails

## First Principles

- A capstone should exercise multiple agent responsibilities at once.
- The goal is not more code volume; the goal is better judgment across the loop.
- A capstone is incomplete unless it includes action policy, fallback policy, and at least one measurable signal.
- Review, block, or fallback behavior should be as explicit as the happy path.

## Core Math

- Grounding coverage:
  $$
  \frac{\text{supported claims}}{\text{claims made}}
  $$
- Expected tool value:
  $$
  p(\text{success}) \cdot \text{success value} - \text{tool cost} - \text{failure penalty}
  $$
- End-to-end latency:
  $$
  \sum_i \text{step latency}_i
  $$

## Minimal Code Mental Model

```python
support = grounded_support_decision(retrieved, memories, tool_profiles, blocked=False, confidence=0.82, grounding_coverage=0.9)
triage = incident_triage_workflow(route_scores, blocked=False, confidence=0.86, attempt=1, max_attempts=2, total_budget_ms=1200, elapsed_ms=300, required_step_budget_ms=250)
```

## Canonical Modules

- `grounded-support-agent`
- `incident-triage-workflow`

## When To Use What

- Start capstones only after prompting, tool use, retrieval, memory, workflows, evaluation, and guardrails feel comfortable.
- Use `grounded-support-agent` to practice retrieval, memory, tool choice, and review/block decisions in one single-agent loop.
- Use `incident-triage-workflow` to practice routing, retries, latency budgeting, escalation, and trace-friendly workflow state.
- Treat these as synthesis modules, not as the first exposure to their component ideas.
