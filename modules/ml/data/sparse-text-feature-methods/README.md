# Sparse Text Feature Methods

> Track: `ml` | Topic: `data`

## Concept

Sparse lexical pipelines usually follow a simple flow: normalize the token
space, convert tokens into sparse counts or weights, optionally hash them into a
fixed-width space, and score which sparse features are most class-informative.

## Math

- $\mathbf{x}_j = \sum_i \mathbf{1}[t_i = v_j]$
- $\mathrm{tfidf}(t, d) = \frac{c_{t,d}}{|d|}\log \frac{N}{\mathrm{df}(t)}$
- $\mathrm{bucket}(x) = h(x) \bmod B$
- $\chi^2 = \sum \frac{(O-E)^2}{E}$

- $t_i$ -- observed token
- $v_j$ -- vocabulary term
- $c_{t,d}$ -- count of term $t$ in document $d$
- $N$ -- number of documents
- $B$ -- number of hash buckets
- $O, E$ -- observed and expected counts

## Key Points

- Count vectors are the simplest lexical baseline.
- TF-IDF downweights globally common terms and upweights document-specific ones.
- The hash trick avoids storing a full vocabulary but introduces collisions.
- Rare-token pruning stabilizes sparse vocabularies before featurization.
- Chi-square scoring is often used to filter sparse lexical features before modeling.

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

## Pitfalls

- Count vectors and TF-IDF ignore word order and semantics.
- Hash collisions can make model behavior harder to inspect.
- Rare-token pruning can drop useful tail signal if the threshold is too aggressive.
- Chi-square scores are featurewise; they do not reason about redundancy between sparse features.

## Run tests

```bash
pytest modules/ml/data/sparse-text-feature-methods/python -q
```
