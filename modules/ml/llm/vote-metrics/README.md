# Vote Metrics

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to summarize how repeated sampled answers agree, fragment, or
form structured alternatives after normalization.

## First Principles

- Repeated sampling reveals whether a model is stable or fragmented.
- Some metrics summarize the winning answer.
- Some summarize diversity or uncertainty.
- Some focus on minority clusters, which matter when disagreement is structured rather than noisy.

## Core Math

- Normalized vote share:
  $$
  p_i = \frac{c_i}{N}
  $$
- Vote entropy:
  $$
  H = -\sum_i p_i \log p_i
  $$
- Majority-vote margin:
  $$
  p_{(1)} - p_{(2)}
  $$

## Minimal Code Mental Model

```python
votes = normalized_vote_counts(answers)
entropy = vote_entropy(answers)
margin = majority_vote_margin(answers)
```

## Function

```python
def normalize_answer(text: str) -> str:
def normalized_vote_counts(answers: list[str]) -> dict[str, int]:
def answer_stability(answers: list[str]) -> float:
def majority_vote_margin(answers: list[str]) -> float:
def vote_entropy(answers: list[str]) -> float:
def answer_uniqueness_rate(answers: list[str]) -> float:
def candidate_diversity(answers: list[str]) -> float:
def top_vote_share(answers: list[str]) -> float:
def consensus_disagreement_rate(answers: list[str]) -> float:
def minority_cluster_entropy(answers: list[str]) -> float:
```

## When To Use What

- Use answer stability for repeated-run consistency.
- Use majority-vote margin or top-vote share when you want a confidence-style summary.
- Use vote entropy when disagreement structure matters more than the winner.
- Use uniqueness or candidate diversity when exploration matters.
- Use minority-cluster entropy when alternatives form meaningful competing groups.

## References

- Wang et al. (2022). [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171)
- Lightman et al. (2023). [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050)

## Run tests

```bash
pytest modules/ml/llm/vote-metrics/python -q
```
