# Consensus Disagreement Rate

> Track: `ml` | Topic: `llm`

## Concept

Consensus disagreement rate measures how much sampled answers disagree with the majority answer.

## Math

$$
\mathrm{disagreement\_rate} = 1 - \max_a \frac{\#\{i : a_i = a\}}{n}
$$

- $a_i$ -- normalized answer from sample $i$
- $n$ -- number of sampled answers

## Key Points

- Lower is better when the goal is stable consensus.
- This complements self-consistency voting by summarizing spread instead of only the winner.
- The module uses lightweight normalization and returns a single rate.

## Function

```python
def consensus_disagreement_rate(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/consensus-disagreement-rate/python -q
```
