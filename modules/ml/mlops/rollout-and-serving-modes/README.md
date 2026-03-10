# Rollout and Serving Modes

> Track: `ml` | Topic: `mlops`

## Purpose

Use this module to learn how modern ML systems choose serving mode and expose a
new model safely.

## First Principles

- Serving mode controls freshness, latency, and throughput.
- Safe rollout is about limiting blast radius before full promotion.
- Shadow and replay evaluate a new model without fully serving its output.
- Canary rollout is a staged traffic-control loop, not just a one-time split.

## Core Math

Canary share:

$$
p_{\text{new}} = \frac{n_{\text{new}}}{n_{\text{total}}}
$$

Backfill replay coverage:

$$
\mathrm{coverage} = \frac{\mathrm{replayed}}{\mathrm{logged}}
$$

Shadow disagreement:

$$
\mathrm{disagreement\_rate} = \frac{1}{n} \sum_{i=1}^{n} \mathbf{1}[\hat{y}^{live}_i \ne \hat{y}^{shadow}_i]
$$

## Minimal Code Mental Model

```python
mode = choose_mode(batch_size=32)
online = is_online(latency_ms=35.0)
canary_share = next_canary_share(current_share=0.1, step=0.1, error_rate=0.01, threshold=0.02)
coverage, mismatch = backfill_replay_metrics(logged, replayed, mismatches)
```

## Functions

```python
def split_traffic(total: int, canary_pct: float) -> tuple[int, int]:
def next_canary_share(current_share: float, step: float, error_rate: float, threshold: float) -> float:
def shadow_disagreement_rate(live_predictions: list[object], shadow_predictions: list[object]) -> tuple[int, float]:
def backfill_replay_metrics(logged_requests: int, replayed_requests: int, mismatched_outputs: int) -> tuple[float, float]:
def is_online(latency_ms: float, threshold_ms: float = 100.0) -> bool:
def choose_mode(batch_size: int) -> str:
```

## When To Use What

- Use online mode when freshness and response latency matter to the user.
- Use batch mode when throughput matters more than per-request latency.
- Use shadow mode before canary when even a small user-facing regression is too risky.
- Use backfill replay when you have historical logs and want offline coverage before live exposure.
- Use canary rollout when you are ready to expose real traffic gradually under guardrails.

## Run tests

```bash
pytest modules/ml/mlops/rollout-and-serving-modes/python -q
```
