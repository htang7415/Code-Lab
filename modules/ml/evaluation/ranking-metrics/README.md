# Ranking Metrics

> Track: `ml` | Topic: `evaluation`

## Concept

Ranking metrics answer different questions about ordered outputs: how early the
first relevant item appears, how much gain is concentrated near the top, how
deep we must scan to cover all relevant labels, and how enriched the top prefix
is relative to the full population.

## Math

- $\mathrm{MRR} = \frac{1}{Q}\sum_{q=1}^{Q}\frac{1}{\mathrm{rank}_q}$
- $\mathrm{DCG@}k = \sum_{i=1}^{k}\frac{2^{rel_i}-1}{\log_2(i+1)}$
- $\mathrm{NDCG@}k = \frac{\mathrm{DCG@}k}{\mathrm{IDCG@}k}$
- $\mathrm{coverage}(x)=\max\{i: rel_i = 1\}$
- $\mathrm{Lift@}k = \frac{\mathrm{Precision@}k}{\mathrm{BaseRate}}$

- $Q$ -- number of queries or ranked examples
- $\mathrm{rank}_q$ -- first relevant rank for query $q$
- $rel_i$ -- relevance at rank $i$
- $k$ -- cutoff rank

## Key Points

- MRR cares only about the first hit.
- NDCG supports graded relevance and rewards early good ranking.
- Coverage error is useful when all relevant labels must eventually appear.
- Lift@k measures how enriched the top-ranked prefix is compared with random selection.

## Function

```python
def mean_reciprocal_rank(relevance_lists: list[list[int]]) -> float:
def ndcg_at_k(relevance: list[float], k: int) -> float:
def coverage_error(relevance_rankings: list[list[int]]) -> float:
def lift_at_k(labels: list[int], k: int) -> float:
```

## Pitfalls

- MRR can hide improvements after the first relevant item.
- NDCG depends on a relevance scale, not just binary hits.
- Coverage error is lower-is-better, unlike most ranking scores.
- Lift@k can look high on rare positives even when recall is low.

## Run tests

```bash
pytest modules/ml/evaluation/ranking-metrics/python -q
```
