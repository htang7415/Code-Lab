# Pairwise Judge Rates

> Track: `ml` | Topic: `llm`

## Concept

Pairwise judge evaluation asks a model or human judge to compare two responses and record whether system A wins, system B wins, or the comparison is a tie.

## Math

$$r_{\mathrm{win}} = \frac{W}{N}, \qquad r_{\mathrm{loss}} = \frac{L}{N}, \qquad r_{\mathrm{tie}} = \frac{T}{N}$$

- $W$ -- number of A-wins
- $L$ -- number of A-losses
- $T$ -- number of ties
- $N$ -- total number of judged comparisons

## Key Points

- Pairwise judging is often easier and more stable than asking for an absolute score.
- Tie rate matters because judges are often uncertain or see negligible quality differences.
- Judge-based evaluation is still a noisy proxy and should be audited for bias.

## Function

```python
def pairwise_judge_rates(outcomes: list[int]) -> tuple[float, float, float]:
```

- `outcomes` uses `1` for an A-win, `-1` for an A-loss, and `0` for a tie

## Run tests

```bash
pytest modules/ml/llm/judge-pairwise/python -q
```
