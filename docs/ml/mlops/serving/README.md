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

- Serving mode and rollout: `rollout-and-serving-modes`
- Throughput and latency health: `service-reliability-metrics`, `request-batching`, `admission-control`
- Systems handoff: `continuous-batching`

## When To Use What

- Use rollout-and-serving modes when choosing between batch vs online paths or when exposing a new model safely.
- Use request batching when throughput matters and small latency inflation is acceptable.
- Use admission control and service-reliability metrics when overload is the main failure mode.
