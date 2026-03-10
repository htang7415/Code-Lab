# Sparse Text Feature Methods

> Track: `ml` | Topic: `data`

## Purpose

Use this module to build simple lexical text baselines before heavier embedding
or transformer pipelines.

## First Principles

- Sparse text features treat text as weighted token occurrences.
- Count vectors are the simplest baseline.
- TF-IDF reweights common vs document-specific terms.
- Hashing avoids storing a full vocabulary but introduces collisions.
- Feature scoring and rare-token pruning stabilize the sparse space before modeling.

## Core Math

- Count vector entry:
  $$
  x_j = \sum_i \mathbf{1}[t_i = v_j]
  $$
- TF-IDF:
  $$
  \mathrm{tfidf}(t, d) = \frac{c_{t,d}}{|d|}\log \frac{N}{\mathrm{df}(t)}
  $$
- Hash bucket:
  $$
  h(x) \bmod B
  $$

## Minimal Code Mental Model

```python
counts = count_vector(tokens, vocabulary)
weights = tf_idf_weights(tokens, document_frequencies, num_documents)
```

## Function

```python
def count_vector(tokens: list[str], vocabulary: list[str]) -> list[int]:
def tf_idf_weights(tokens: list[str], document_frequencies: dict[str, int], num_documents: int) -> dict[str, float]:
def hashed_feature_counts(tokens: list[str], num_buckets: int) -> list[int]:
def chi_square_feature_score(
    present_positive: int,
    present_negative: int,
    absent_positive: int,
    absent_negative: int,
) -> float:
def prune_rare_tokens(tokens: list[str], min_count: int, unk_token: str = "__UNK__") -> list[str]:
```

## When To Use What

- Use count vectors as the simplest lexical baseline.
- Use TF-IDF when document-specific terms matter more than raw frequency.
- Use hashing when you need fixed-width features without a maintained vocabulary.
- Use rare-token pruning and chi-square scoring when the sparse space is too noisy or too wide.

## Run tests

```bash
pytest modules/ml/data/sparse-text-feature-methods/python -q
```
