# Monte Carlo Tree Search UCT Score

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Monte Carlo Tree Search balances exploration and exploitation during tree expansion.
This module focuses on the UCT score used to choose which child to visit next.

## Math

$$\mathrm{UCT} = \bar{Q} + c \sqrt{\frac{\log N}{n}}$$

- $\bar{Q}$ -- average value of the child node
- $c$ -- exploration constant
- $N$ -- parent visit count
- $n$ -- child visit count

## Key Points

- High-value children are favored through the average value term.
- Rarely visited children are favored through the exploration bonus.
- Unvisited children are typically explored before any fully scored child.

## Function

```python
def uct_score(
    value_sum: float,
    parent_visits: int,
    child_visits: int,
    exploration: float = 1.4142135623730951,
) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/monte-carlo-tree-search/python -q
```
