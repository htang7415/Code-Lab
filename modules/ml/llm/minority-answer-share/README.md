# Minority Answer Share

> Track: `ml` | Topic: `llm`

## Concept

Minority answer share measures the fraction of normalized answer mass outside the largest answer cluster.

## Math

If the largest normalized answer cluster has share $p_{(1)}$:

$$
\mathrm{MinorityAnswerShare} = 1 - p_{(1)}
$$

## Key Points

- This summarizes how much mass lies away from the dominant answer.
- Higher values indicate more fragmented sampled answers.
- This module normalizes answers before counting clusters.

## Function

```python
def minority_answer_share(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-answer-share/python -q
```
