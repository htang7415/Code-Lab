# ML Serving

Serving is the operational layer between a trained model and a real workload.

## Purpose

Use this page to reason about:
- offline vs online modes
- rollout strategy
- batching and queueing
- admission and latency control

## First Principles

- Serving mode changes both cost and product behavior.
- Canary and shadow workflows exist to fail small before failing large.
- Queueing and batching trade throughput against latency.
- Admission control matters because an overloaded correct system is still a bad system.

## Core Math

- Throughput:
  $$
  \frac{\text{requests or tokens}}{\text{second}}
  $$
- Queueing pressure rises when arrival rate approaches or exceeds service rate.

## Minimal Code Mental Model

```python
if queue_delay > budget:
    reject_or_degrade(request)
else:
    batch.append(request)
```

## Canonical Modules

- Serving mode: `offline-online-inference`, `batch-vs-realtime`
- Rollout safety: `canary-deployment`, `canary-rollout`, `online-shadow-mode`
- Throughput control: `request-batching`, `admission-control`, `queue-delay`, `request-sla`
- Systems handoff: `continuous-batching`

## When To Use What

- Use offline or batch inference when freshness is weakly coupled to user experience.
- Use canary or shadow rollout before full replacement.
- Use request batching when throughput matters and small latency inflation is acceptable.
- Use admission control and queue-delay metrics when overload is the main failure mode.
