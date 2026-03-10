# Planning

Planning is the layer that turns a broad goal into ordered steps the agent can execute and track.

## Purpose

Use this page to understand:
- when a task needs an explicit plan
- how to track unfinished work
- why short plans beat vague reasoning loops

## First Principles

- Planning is most useful when a task has multiple dependent steps.
- A plan should be explicit enough to inspect and update.
- The next action should come from plan state, not just free-form generation.

## Minimal Code Mental Model

```python
plan = make_plan("Prepare launch report", ["collect metrics", "write summary", "send report"])
step = next_pending_step(plan)
plan = mark_step_done(plan, 0)
```

## Canonical Modules

- Main step-tracking pattern: `plan-act-loop`

## When To Use What

- Start with `plan-act-loop` when the task needs state and ordering.
- Keep plans short and concrete before adding branching or multi-agent coordination.
