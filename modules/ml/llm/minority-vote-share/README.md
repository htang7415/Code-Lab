# Minority Vote Share

> Track: `ml` | Topic: `llm`

## Concept

Minority vote share measures the fraction of normalized vote mass outside the largest answer cluster.

## Math

If the largest normalized answer cluster has vote share $p_{(1)}$:

$$
\mathrm{MinorityVoteShare} = 1 - p_{(1)}
$$

## Key Points

- This is the complement of the dominant vote share.
- Higher values mean the answer distribution is more fragmented.
- This module normalizes answers before counting votes.

## Function

```python
def minority_vote_share(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-vote-share/python -q
```
