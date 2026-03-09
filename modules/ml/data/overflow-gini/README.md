# Overflow Gini

> Track: `ml` | Topic: `data`

## Concept

Overflow Gini measures how unevenly overflow is distributed across examples in a batch.

## Math

For overflow amounts $o_i = \max(0, l_i - L)$ sorted as $o_{(1)} \le \dots \le o_{(N)}$:

$$
G = \frac{\sum_{i=1}^{N} (2i - N - 1) o_{(i)}}{N \sum_{i=1}^{N} o_{(i)}}
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length

## Key Points

- A value near `0` means overflow is spread relatively evenly.
- A value near `1` means a few examples dominate overflow severity.
- This module returns `0` when there is no overflow at all.

## Function

```python
def overflow_gini(lengths: list[int], max_length: int) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-gini/python -q
```
