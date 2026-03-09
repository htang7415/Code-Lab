# Nonmajority Vote Share

> Track: `ml` | Topic: `llm`

## Concept

Nonmajority vote share measures what fraction of normalized vote mass is not assigned to the top answer.

## Math

If the top normalized answer has vote share $p_{(1)}$:

$$
\mathrm{NonmajorityVoteShare} = 1 - p_{(1)}
$$

## Key Points

- This is another name for vote tail mass.
- Higher values mean more vote mass lies outside the winner.
- This module normalizes answers before counting votes.

## Function

```python
def nonmajority_vote_share(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/nonmajority-vote-share/python -q
```
