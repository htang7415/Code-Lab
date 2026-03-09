# BM25 Ranking Score

> Track: `ml` | Topic: `llm`

## Concept

BM25 is a classic lexical retrieval score that improves on TF-IDF by saturating term frequency and normalizing for document length.

## Math

$$\mathrm{BM25}(q, d) = \sum_{t \in q} \mathrm{idf}(t)\,\frac{f(t, d)(k_1 + 1)}{f(t, d) + k_1 \left(1 - b + b\frac{|d|}{\mathrm{avgdl}}\right)}$$

$$\mathrm{idf}(t) = \log \left(1 + \frac{N - \mathrm{df}(t) + 0.5}{\mathrm{df}(t) + 0.5}\right)$$

- $f(t, d)$ -- term frequency of query term $t$ in document $d$
- $|d|$ -- document length
- $\mathrm{avgdl}$ -- average document length in the corpus
- $N$ -- number of documents
- $\mathrm{df}(t)$ -- document frequency of term $t$

## Key Points

- BM25 is a strong lexical baseline for retrieval and reranking.
- Repeated term matches help, but with diminishing returns.
- Longer documents are normalized so they are not rewarded just for containing more words.

## Function

```python
def bm25_score(
    query_terms: list[str],
    document_terms: list[str],
    document_frequencies: dict[str, int],
    num_documents: int,
    avg_doc_length: float,
    k1: float = 1.5,
    b: float = 0.75,
) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/bm25-ranking/python -q
```
