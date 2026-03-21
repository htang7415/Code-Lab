# Cross-Encoder Vs Bi-Encoder

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to choose between fast embedding retrieval and slower pairwise
reranking for modern RAG and search systems.

## First Principles

- A bi-encoder embeds the query and document separately.
- Because document embeddings can be precomputed, bi-encoders scale to large
  corpora.
- A cross-encoder reads the query and document together, so it can model
  token-level interactions across the pair.
- That joint scoring often improves top-k precision, but it costs one forward
  pass per query-document pair.
- Real systems often retrieve candidates with a bi-encoder and rerank the
  shortlist with a cross-encoder.

## Core Math

Bi-encoder scoring:

$$
e_q = f(q), \quad e_d = g(d), \quad s_{\text{bi}}(q, d) = \cos(e_q, e_d)
$$

Cross-encoder scoring:

$$
s_{\text{cross}}(q, d) = h([q ; d])
$$

Cross-encoder pair count if every query is scored against all `N` documents:

$$
\mathrm{FullPairs} = QN
$$

Cross-encoder pair count when reranking only top-`k` candidates per query:

$$
\mathrm{RerankPairs} = Qk
$$

Pair reduction from reranking instead of full-corpus scoring:

$$
\mathrm{Reduction} = 1 - \frac{k}{N}
$$

- $Q$ -- number of queries
- $N$ -- corpus size
- $k$ -- number of candidates sent to reranking

## From Math To Code

- Use cosine similarity as the bi-encoder retrieval proxy.
- Use token overlap plus order sensitivity as a toy cross-encoder proxy.
- Compare full-corpus pair counts against reranking pair counts.
- Treat that pair-count gap as the main reason hybrid retrieval stacks exist.

## Minimal Code Mental Model

```python
bi = bi_encoder_score([1.0, 0.0], [0.8, 0.2])
cross = cross_encoder_score(["refund", "policy"], ["refund", "policy", "approved"])
full_pairs = cross_encoder_full_corpus_pairs(num_queries=100, corpus_size=1_000_000)
rerank_pairs = bi_encoder_rerank_pairs(num_queries=100, candidate_k=50)
reduction = rerank_pair_reduction(corpus_size=1_000_000, candidate_k=50)
```

## Functions

```python
def cosine_similarity(left: list[float], right: list[float]) -> float:
def bi_encoder_score(query_embedding: list[float], document_embedding: list[float]) -> float:
def cross_encoder_score(query_tokens: list[str], document_tokens: list[str]) -> float:
def cross_encoder_full_corpus_pairs(num_queries: int, corpus_size: int) -> int:
def bi_encoder_rerank_pairs(num_queries: int, candidate_k: int) -> int:
def rerank_pair_reduction(corpus_size: int, candidate_k: int) -> float:
```

## When To Use What

- Use a bi-encoder when you need cheap retrieval over a large corpus.
- Use a cross-encoder when the candidate set is already small and final ranking
  quality matters more than throughput.
- Use bi-encoder plus cross-encoder reranking when you need both scale and high
  top-k precision.
- Use `retrieval-metrics` after deployment to verify that the extra reranking
  cost actually improves ranking quality.

## References

- Reimers and Gurevych (2019). [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084)
- Nogueira and Cho (2019). [Passage Re-ranking with BERT](https://arxiv.org/abs/1901.04085)
- Karpukhin et al. (2020). [Dense Passage Retrieval for Open-Domain Question Answering](https://arxiv.org/abs/2004.04906)

## Run tests

```bash
pytest modules/ml/llm/cross-encoder-vs-bi-encoder/python -q
```
