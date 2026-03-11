# Run Sampling

> Track: `ai-agents` | Topic: `observability`

## Concept

Run sampling keeps enough traces to debug the system without storing every run.

## Key Points

- Sampling is a cost-control decision, not an excuse to lose important failures.
- A deterministic rule makes repeated inspection easier than random per-request flips.
- Always keep critical or failing runs even when the default sample rate is low.

## Minimal Code Mental Model

```python
keep = should_sample_run("run_42", 0.2)
sampled = sampled_run_ids(["run_1", "run_2", "run_3"], 0.5)
rate = realized_sample_rate(["run_1", "run_2"], 0.5)
```

## Function

```python
def should_sample_run(run_id: str, sample_rate: float) -> bool:
def sampled_run_ids(run_ids: list[str], sample_rate: float) -> list[str]:
def realized_sample_rate(run_ids: list[str], sample_rate: float) -> float:
```

## Run tests

```bash
pytest modules/ai-agents/observability/run-sampling/python -q
```
