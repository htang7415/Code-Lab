# LLM Evaluation

LLM evaluation mixes language-model likelihood, task scoring, and model-judge style comparisons.

## Leaf Guides

- Vote and minority-cluster metrics (`docs/ml/llm/vote-metrics`)

## Current Anchors

- Retrieval metrics family (`modules/ml/llm/retrieval-metrics`)
- Perplexity (`modules/ml/llm/perplexity`)
- MMLU-style evaluation (`modules/ml/llm/mmlu-evaluation`)
- Normalized exact match (`modules/ml/llm/exact-match`)
- Answer verification (`modules/ml/llm/answer-verification`)
- Self-consistency voting (`modules/ml/llm/self-consistency-voting`)
- Judge calibration (`modules/ml/llm/judge-calibration`)
- Consensus disagreement rate (`modules/ml/llm/consensus-disagreement-rate`)
- BLEU / METEOR overlap (`modules/ml/llm/bleu-meteor`)
- Pass@k (`modules/ml/llm/pass-at-k`)
- Retrieval Recall@k (`modules/ml/llm/retrieval-recall-at-k`)
- Retrieval Precision@k (`modules/ml/llm/retrieval-precision-at-k`)
- Retrieval F1@k (`modules/ml/llm/retrieval-f1-at-k`)
- Retrieval HitRate@k (`modules/ml/llm/retrieval-hit-rate`)
- Rerank gain (`modules/ml/llm/rerank-gain`)
- Rerank disagreement rate (`modules/ml/llm/rerank-disagreement-rate`)
- Mean reciprocal rank (`modules/ml/evaluation/mean-reciprocal-rank`)
- NDCG (`modules/ml/evaluation/ndcg`)
- Reciprocal rank for one query (`modules/ml/llm/reciprocal-rank-metric`)
- Pairwise judge rates (`modules/ml/llm/judge-pairwise`)
- Judge agreement matrix (`modules/ml/llm/judge-agreement-matrix`)
- Reranker metrics (`modules/ml/llm/reranker-metrics`)
- Bradley-Terry pairwise probability (`modules/ml/evaluation/bradley-terry-ranking`)

## Concepts to Cover Well

- Perplexity and token-level likelihood
- Exact match and normalized string matching
- Answer verification with multiple acceptable references
- Answer stability across repeated decoding runs
- Majority-vote margin between the top two normalized answers
- Vote entropy over normalized answer counts
- Vote concentration of the most common normalized answer
- Top vote share for the most common normalized answer
- Runner-up vote share for the second-most common normalized answer
- Answer uniqueness rate across normalized sampled answers
- Answer repeat rate as the complement of uniqueness
- Answer mode count for the largest normalized vote block
- Answer frequency tables for direct vote inspection
- Vote frequency gap between the top two normalized answers
- Vote imbalance normalized by the top-two vote mass
- Vote tail mass outside the top normalized answer
- Nonmajority vote share outside the winning normalized answer
- Minority vote share outside the dominant normalized answer cluster
- Minority answer share outside the largest normalized answer cluster
- Minority cluster count outside the dominant normalized answer cluster
- Minority cluster share outside the dominant normalized answer cluster
- Minority cluster mode as the typical size of alternative normalized answer groups
- Minority cluster entropy over the alternative normalized answer groups
- Minority cluster top share as the dominant alternative cluster within minority mass
- Minority cluster dominance as the gap between the strongest and second strongest minority clusters
- Minority cluster balance as evenness across the minority normalized answer groups
- Minority cluster tail entropy over the lower-mass minority clusters after removing the strongest alternative
- Minority cluster residual mass as the answer share left after removing the strongest minority alternative
- Minority cluster remainder ratio as the fraction of minority mass left after removing the strongest alternative
- Minority cluster tail balance as evenness across the residual low-mass minority clusters
- Minority cluster tail gap as the dominance gap between the two strongest residual tail clusters
- Minority cluster tail share as the absolute answer share of the strongest residual tail cluster
- Minority cluster tail top share as the strongest residual tail cluster's share within tail mass
- Minority cluster tail ratio as residual minority mass relative to the strongest minority cluster
- Minority cluster tail concentration as a Herfindahl-style dominance score over the residual tail
- Minority cluster tail entropy gap as the shortfall from a perfectly uniform residual tail
- Self-consistency voting across multiple sampled traces
- Candidate diversity across multiple sampled candidates
- Judge confidence aligned with correctness
- Consensus spread across sampled answers
- BLEU / METEOR style overlap metrics
- Pass@k for code and reasoning tasks
- Benchmark-style scoring such as MMLU variants
- Judge-based and pairwise preference evaluation
- Judge agreement tables before chance-corrected agreement metrics
- Bradley-Terry style pairwise ranking models
- Retrieval and reranker metrics such as MRR and Recall@k
- Retrieval precision when early purity matters more than coverage
- Retrieval F1 when precision and recall must be balanced
- Retrieval hit rate when any successful retrieval is enough
- Rerank gain relative to a baseline ranking
- Rerank disagreement as an ordering-change summary
- Graded ranking metrics such as NDCG
- Query-level reciprocal rank before averaging into MRR
