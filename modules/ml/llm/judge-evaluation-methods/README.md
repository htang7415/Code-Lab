# Judge Evaluation Methods

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to learn the main judge-based evaluation tools in one place:
pairwise win/loss summaries, judge calibration, and judge agreement.

## First Principles

- Judge-based evaluation is useful when exact references are weak or style matters.
- Pairwise judging is often easier than absolute scoring because the judge only needs to compare two answers.
- Confidence is only useful if it tracks whether the judge is actually right.
- Agreement matters because one strong judge is still a noisy proxy.

## Core Math

Pairwise outcome rates:

$$
r_{\mathrm{win}} = \frac{W}{N}, \qquad r_{\mathrm{loss}} = \frac{L}{N}, \qquad r_{\mathrm{tie}} = \frac{T}{N}
$$

Calibration gap:

$$
\mathrm{gap} = \frac{1}{n} \sum_{i=1}^{n} \left| c_i - y_i \right|
$$

Agreement matrix entry:

$$
A_{ij} = \frac{1}{N} \sum_{n=1}^{N} \mathbf{1}[d_{i,n} = d_{j,n}]
$$

## Minimal Code Mental Model

```python
wins, losses, ties = pairwise_judge_rates(outcomes)
gap = judge_calibration_gap(confidences, correctness)
agreement = judge_agreement_matrix([judge_a, judge_b, judge_c])
```

## Functions

```python
def pairwise_judge_rates(outcomes: list[int]) -> tuple[float, float, float]:
def judge_calibration_gap(confidences: list[float], correctness: list[int]) -> float:
def judge_agreement_matrix(judge_decisions: list[list[int]]) -> list[list[float]]:
```

## When To Use What

- Use pairwise rates when you want the simplest summary of judge wins, losses, and ties.
- Use judge calibration when the judge emits confidence and you have gold labels for whether its verdict was correct.
- Use agreement matrices when comparing multiple judges, prompts, or judging templates over the same examples.
- Use `bradley-terry-ranking` as the next step when pairwise outcomes need to become a global latent ranking.

## References

- Zheng et al. (2023). [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685)
- Liu et al. (2023). [G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment](https://arxiv.org/abs/2303.16634)
- Lightman et al. (2023). [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050)

## Run tests

```bash
pytest modules/ml/llm/judge-evaluation-methods/python -q
```
