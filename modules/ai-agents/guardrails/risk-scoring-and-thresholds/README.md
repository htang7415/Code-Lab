# Risk Scoring and Thresholds

> Track: `ai-agents` | Topic: `guardrails`

## Concept

Risk scoring and thresholds make guardrail decisions explicit by aggregating a few normalized risk signals into one score and mapping that score to allow, review, or block.

## Key Points

- A weighted mean is often enough: `risk = sum(weight * signal) / sum(weight)`.
- Signals should be normalized to the same range, usually `0` to `1`.
- Separate review and block thresholds make policy decisions easier to audit.

## Core Math

- Weighted risk score:
  $$
  \frac{\sum_i w_i s_i}{\sum_i w_i}
  $$
- Threshold order:
  $$
  \tau_{\text{review}} < \tau_{\text{block}}
  $$

## Minimal Code Mental Model

```python
weights = {"untrusted_input": 0.4, "side_effect": 0.4, "secret_access": 0.2}
score = weighted_risk_score(signals, weights)
active = active_risk_signals(signals, min_signal=0.7)
decision = risk_decision(score, review_threshold=0.5, block_threshold=0.8)
```

## Function

```python
def weighted_risk_score(signals: dict[str, float], weights: dict[str, float]) -> float:
def active_risk_signals(signals: dict[str, float], min_signal: float) -> list[str]:
def risk_decision(score: float, review_threshold: float, block_threshold: float) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/guardrails/risk-scoring-and-thresholds/python -q
```
