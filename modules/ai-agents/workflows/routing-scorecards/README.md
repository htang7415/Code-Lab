# Routing Scorecards

> Track: `ai-agents` | Topic: `workflows`

## Concept

Routing scorecards make route selection explicit by scoring each candidate route on a small set of signals instead of relying on vague prompt intuition alone.

## Key Points

- A weighted route score is often enough: `score = sum(weight * signal) / sum(weight)`.
- Route signals should stay small and interpretable, such as task fit, tool readiness, or latency fit.
- If the best score is too weak or too close to the next route, review is safer than guessing.

## Core Math

- Weighted route score:
  $$
  \frac{\sum_i w_i s_i}{\sum_i w_i}
  $$
- Selection margin:
  $$
  \text{best score} - \text{runner-up score}
  $$

## Minimal Code Mental Model

```python
weights = {"task_fit": 0.5, "tool_readiness": 0.3, "latency_fit": 0.2}
scored = score_routes(candidates, weights)
route = scorecard_route(candidates, weights, min_score=0.75, min_margin=0.05)
```

## Function

```python
def route_score(route_signals: dict[str, float], signal_weights: dict[str, float]) -> float:
def score_routes(
    route_to_signals: dict[str, dict[str, float]],
    signal_weights: dict[str, float],
) -> list[dict[str, object]]:
def scorecard_route(
    route_to_signals: dict[str, dict[str, float]],
    signal_weights: dict[str, float],
    min_score: float,
    min_margin: float = 0.0,
) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/workflows/routing-scorecards/python -q
```
