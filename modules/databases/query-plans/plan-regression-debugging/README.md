# Plan Regression Debugging

> Track: `databases` | Topic: `query-plans`

## Concept

Plan regression debugging compares a known-good plan to a current plan and looks for new full scans, lost indexes, or new sorts.

## Key Points

- Query latency often regresses because the plan shape changed.
- The first question is usually not “why is it slow?” but “what changed in the plan?”
- Losing an index or gaining a temp sort is often enough to explain a major slowdown.
- Plan summaries make regressions easier to compare than raw multiline plans.

## Minimal Code Mental Model

```python
baseline = summarize_plan(["SEARCH runs USING INDEX idx_runs_workspace_created"])
current = summarize_plan(["SCAN runs", "USE TEMP B-TREE FOR ORDER BY"])
signals = regression_signals(baseline, current)
```

## Function

```python
def summarize_plan(plan_details: list[str]) -> dict[str, bool]:
def regression_signals(
    baseline: dict[str, bool],
    current: dict[str, bool],
) -> list[str]:
def plan_regressed(
    baseline: dict[str, bool],
    current: dict[str, bool],
) -> bool:
```

## Run tests

```bash
pytest modules/databases/query-plans/plan-regression-debugging/python -q
```
