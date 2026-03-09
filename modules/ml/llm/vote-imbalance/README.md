# Vote Imbalance

> Track: `ml` | Topic: `llm`

## Concept

Vote imbalance measures how dominant the top normalized answer is relative to the runner-up, normalized by the vote mass of those top two answers.

## Math

For top two normalized answer counts $c_{(1)} \ge c_{(2)}$:

$$
\mathrm{VoteImbalance} = \frac{c_{(1)} - c_{(2)}}{c_{(1)} + c_{(2)}}
$$

If there is only one unique answer, this module treats the runner-up count as zero.

## Key Points

- This is a count-normalized gap, not a raw count difference.
- Larger values mean the vote has a clearer winner.
- This module normalizes answers before counting votes.

## Function

```python
def vote_imbalance(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/vote-imbalance/python -q
```
