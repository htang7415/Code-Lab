# Vote Tail Mass

> Track: `ml` | Topic: `llm`

## Concept

Vote tail mass measures the fraction of normalized vote mass not assigned to the top answer.

## Math

If the top normalized answer has vote share $p_{(1)}$:

$$
\mathrm{VoteTailMass} = 1 - p_{(1)}
$$

## Key Points

- Tail mass is a simple ambiguity metric for repeated decoding.
- It is the complement of top vote share.
- This module normalizes answers before counting votes.

## Function

```python
def vote_tail_mass(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/vote-tail-mass/python -q
```
