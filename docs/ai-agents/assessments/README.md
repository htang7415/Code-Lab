# Assessments

Use this page to check whether the agent track is changing how you design agent loops, not just how many modules you have read.

## Purpose

Use this page to test whether you can:
- explain when an agent should answer, tool-call, review, or block
- keep routing, latency, and risk rules explicit
- choose the smallest useful metrics for an agent workflow
- decide whether you are ready for capstones

## First Principles

- Agent readiness is about explicit decision rules, not prompt confidence.
- A strong answer should include both the action policy and the fallback or review policy.
- Evaluation, observability, and guardrails should be part of the design before scaling usage.

## Core Math

- Success rate:
  $$
  \frac{\text{successful runs}}{\text{runs observed}}
  $$
- Route or policy score:
  $$
  \text{value} - \text{cost} - \text{risk penalty}
  $$
- Remaining latency budget:
  $$
  \text{total budget} - \text{elapsed} - \text{reserved response}
  $$

## Minimal Code Mental Model

```python
score = success_rate / mean_cost
route = choose_route(route_scores, min_margin=0.1)
ready = route is not None and latency_budget_ms > 0 and risk_score < 0.8
```

## Section Checks

- Prompting: Can you separate system behavior, user task, and constraints without wasting prompt budget?
- Tool Use: Can you justify answer vs tool vs review with expected value, validation, or failure downside?
- RAG: Can you say when weak grounding coverage means abstain or retrieve more?
- Memory: Can you explain when to use short summaries versus retrieval-backed memory and how weak memories should be evicted?
- Planning: Can you explain which steps fit under budget and when the planner should stop or replan?
- Workflows: Can you explain route choice, retry budget, and escalation path in one workflow?
- Observability: Can you pick one success metric, one latency metric, and one failure-source summary for the loop?
- Evaluation: Can you compare two variants with calibration, significance, or cost-quality reasoning instead of raw win rate only?
- Guardrails: Can you justify allow, review, or block with explicit thresholds or expected costs?
- Multi-Agent: Can you explain why role split and delegation budget help more than one stronger single-agent loop?

## Capstone Readiness

You are ready for capstones when you can do all of these:

- write a short action policy before implementation
- name the active state the agent should keep
- explain when the agent should answer directly, call a tool, escalate, or block
- choose one metric that would prove the workflow is working
- describe the latency or cost budget
- describe the review or fallback path

## Graduation Check

The track is working if you can review a proposed agent workflow and answer these six questions quickly:

1. What state should stay active?
2. Which action is worth taking next?
3. What should trigger review, fallback, or block?
4. What would we measure across runs?
5. What budget constrains the loop?
6. What changes if the workflow splits across workers?

## Weak Signals

You probably need another pass through the foundations if:

- you add memory before a simple tool loop is stable
- you add retries without a retry budget or escalation path
- you trust confidence without calibration or grounding checks
- you add workers without a clear role split
- you cannot say when a request should be blocked or reviewed
