# ML Coverage Roadmap

Goal: make the ML track feel complete against a broad problem-bank style curriculum without mirroring hundreds of narrow one-off problems.
This roadmap is driven by the live Deep-ML title list captured in `artifacts/deepml/problem_titles.md`.

## First Principle

- Fill docs gaps before adding lots of new modules.
- Add new modules only for canonical concepts not already represented.
- Prefer one module that teaches a family over several tiny variants.

## Added in This Pass

Docs added:

- `docs/ml/README.md`
- `docs/ml/fundamentals/prob/README.md`
- `docs/ml/fundamentals/stats/README.md`
- `docs/ml/data/preprocessing/README.md`
- `docs/ml/models/linear/README.md`
- `docs/ml/models/trees/README.md`
- `docs/ml/evaluation/calibration/README.md`
- `docs/ml/llm/evaluation/README.md`
- `docs/ml/llm/inference-serving/README.md`
- `docs/ml/systems/gpu/README.md`
- `docs/ml/systems/distributed/README.md`

Modules added:

- `modules/ml/evaluation/expected-calibration-error`
- `modules/ml/data/imputation`
- `modules/ml/models/gaussian-mixture-model-em`
- `modules/ml/llm/perplexity`
- `modules/ml/llm/kv-cache`
- `modules/ml/systems/roofline-analysis`
- `modules/ml/data/smote`
- `modules/ml/models/gradient-boosting`
- `modules/ml/llm/speculative-decoding`
- `modules/ml/llm/prefix-cache`
- `modules/ml/systems/continuous-batching`
- `modules/ml/models/isolation-forest`
- `modules/ml/models/kernel-pca`
- `modules/ml/models/xgboost-objective`
- `modules/ml/llm/mmlu-evaluation`
- `modules/ml/llm/pass-at-k`
- `modules/ml/systems/context-parallelism`
- `modules/ml/systems/tensor-parallelism`
- `modules/ml/systems/prefix-cache-metrics`
- `modules/ml/generative/ddpm-sampling`
- `modules/ml/data/outlier-detection`
- `modules/ml/systems/expert-parallelism`
- `modules/ml/systems/chunked-prefill`
- `modules/ml/evaluation/confidence-intervals`
- `modules/ml/llm/exact-match`
- `modules/ml/llm/judge-pairwise`
- `modules/ml/models/lle`
- `modules/ml/models/tsne-gradient`
- `modules/ml/models/bic-aic`
- `modules/ml/llm/bleu-meteor`
- `modules/ml/generative/ddim-sampling`
- `modules/ml/data/tf-idf`
- `modules/ml/llm/bm25-ranking`
- `modules/ml/reinforcement-learning/monte-carlo-tree-search`
- `modules/ml/reinforcement-learning/first-visit-monte-carlo-prediction`
- `modules/ml/reinforcement-learning/n-step-td-prediction`
- `modules/ml/data/feature-scaling`
- `modules/ml/llm/beam-search`
- `modules/ml/llm/top-p-sampling`
- `modules/ml/llm/temperature-sampling`
- `modules/ml/reinforcement-learning/eligibility-traces`
- `modules/ml/evaluation/bootstrap-intervals`
- `modules/ml/optimization/warmup-cosine-decay`
- `modules/ml/llm/tokenizer-comparison`
- `modules/ml/reinforcement-learning/importance-sampling`
- `modules/ml/llm/top-k-sampling`

## Top 10 Docs to Write Next

- `docs/ml/fundamentals/math/README.md`: connect Jacobian, Hessian, SVD, PCA, and optimization geometry in one place.
- `docs/ml/representation/embeddings/README.md`: connect cosine similarity, autoencoders, contrastive loss, and representation quality.
- `docs/ml/generative/diffusion/README.md`: organize DDPM, DDIM, guidance, and noise schedules.
- `docs/ml/optimization/schedules/README.md`: unify warmup, cosine decay, step decay, and restart intuition.
- `docs/ml/mlops/monitoring/README.md`: connect latency, drift, health metrics, and production alerting.
- `docs/ml/mlops/serving/README.md`: connect canaries, batching, SLAs, and online inference operations.
- `docs/ml/llm/tokenization/README.md`: connect character tokenization, BPE, and tokenizer-dependent evaluation.
- `docs/ml/llm/alignment/README.md`: connect SFT, RLHF, DPO, KL penalties, and PTX anchoring.
- `docs/ml/evaluation/uncertainty/README.md`: cover predictive uncertainty, confidence, and when probability estimates are actionable.
- `docs/ml/reinforcement-learning/rl-for-llm/README.md`: connect reward modeling, PPO-style alignment, and GRPO/GSPO ideas.

## Top 10 New Modules to Add Next

`modules/ml/generative/diffusion-guidance-tradeoffs` already covers the classifier-free guidance idea, so it is no longer tracked as a separate module.
`modules/ml/mlops/ab-testing`, `modules/ml/mlops/canary-deployment`, `modules/ml/mlops/feature-drift-psi`, and `modules/ml/representation/contrastive-loss` already cover the corresponding title areas, so they are no longer tracked as missing.

- `modules/ml/evaluation/permutation-test`: inferred experiment-analysis gap beyond rate calculators.
- `modules/ml/evaluation/isotonic-calibration`: inferred calibration gap beyond ECE.
- `modules/ml/llm/reranker-metrics`: inferred retrieval-evaluation gap after BM25.
- `modules/ml/systems/expert-load-balancing`: inferred MoE systems gap beyond routing and dispatch.
- `modules/ml/data/missing-indicator`: inferred preprocessing gap complementary to imputation.
- `modules/ml/evaluation/bradley-terry-ranking`: exact Deep-ML title match for pairwise ranking models.
- `modules/ml/mlops/request-sla`: inferred serving-metrics gap complementary to existing SLA basics.
- `modules/ml/llm/sampling-pipeline`: exact Deep-ML title match for combined temperature plus top-k plus top-p logic.
- `modules/ml/data/robust-scaling`: inferred preprocessing gap beyond z-score and min-max scaling.
- `modules/ml/llm/retrieval-fusion`: inferred retrieval systems gap after BM25.

## Second Wave After That

- `modules/ml/evaluation/bradley-terry-ranking`
- `modules/ml/mlops/request-sla`
- `modules/ml/llm/sampling-pipeline`
- `modules/ml/data/robust-scaling`
- `modules/ml/llm/retrieval-fusion`
- `modules/ml/evaluation/wilson-interval`
- `modules/ml/reinforcement-learning/td-lambda`
- `modules/ml/evaluation/ab-test-analysis`
- `modules/ml/mlops/canary-rollout`
- `modules/ml/mlops/drift-detection`
- `modules/ml/representation/pairwise-ranking-loss`
