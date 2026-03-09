# Vote Frequency Gap

> Track: `ml` | Topic: `llm`

## Concept

Vote frequency gap measures the raw count gap between the most common and second-most common normalized answers.

## Math

For sorted normalized answer counts $c_{(1)} \ge c_{(2)} \ge \dots$:

$$
\mathrm{VoteFrequencyGap} = c_{(1)} - c_{(2)}
$$

If there is only one unique answer, this module treats the runner-up count as zero.

## Key Points

- This is the count analogue of majority-vote margin.
- Larger gaps mean a clearer winner in repeated decoding.
- This module normalizes answers before counting votes.

## Function

```python
def vote_frequency_gap(answers: list[str]) -> int:
```

## Run tests

```bash
pytest modules/ml/llm/vote-frequency-gap/python -q
```
