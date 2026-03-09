# Backfill Replay

> Track: `ml` | Topic: `mlops`

## Concept

Backfill replay runs historical requests through a candidate system offline to check coverage and mismatch rate before rollout.

## Math

$$
\mathrm{coverage} = \frac{\mathrm{replayed}}{\mathrm{logged}}
$$

$$
\mathrm{mismatch\_rate} = \frac{\mathrm{mismatches}}{\mathrm{replayed}}
$$

- $\mathrm{logged}$ -- total historical requests available
- $\mathrm{replayed}$ -- requests successfully replayed
- $\mathrm{mismatches}$ -- replayed requests whose outputs disagree with the baseline

## Key Points

- Backfill replay is an offline validation pattern, unlike online shadow mode.
- Coverage matters because sparse or broken replays can hide regressions.
- Mismatch rate helps quantify output drift before exposing traffic.

## Function

```python
def backfill_replay_metrics(
    logged_requests: int,
    replayed_requests: int,
    mismatched_outputs: int,
) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/mlops/backfill-replay/python -q
```
