# TF-IDF Weights

> Track: `ml` | Topic: `data`

## Concept

TF-IDF combines term frequency inside one document with inverse document frequency across a corpus.
It is a simple lexical feature baseline for text classification and retrieval.

## Math

$$\mathrm{tfidf}(t, d) = \frac{c_{t,d}}{|d|} \log \frac{N}{\mathrm{df}(t)}$$

- $c_{t,d}$ -- count of term $t$ in document $d$
- $|d|$ -- total number of tokens in document $d$
- $N$ -- number of documents in the corpus
- $\mathrm{df}(t)$ -- number of documents containing term $t$

## Key Points

- Terms get more weight when they are frequent in the current document but rare in the corpus.
- TF-IDF ignores word order and meaning; it is purely lexical.
- Despite its simplicity, it remains a strong baseline for many text tasks.

## Function

```python
def tf_idf_weights(
    tokens: list[str],
    document_frequencies: dict[str, int],
    num_documents: int,
) -> dict[str, float]:
```

## Run tests

```bash
pytest modules/ml/data/tf-idf/python -q
```
