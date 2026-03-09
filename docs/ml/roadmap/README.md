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

- `modules/ml/evaluation/ab-test-analysis`: exact Deep-ML title match for model-comparison statistics.
- `modules/ml/data/feature-scaling`: exact Deep-ML title match for preprocessing standardization basics.
- `modules/ml/mlops/canary-rollout`: grounded in the Deep-ML canary deployment health title.
- `modules/ml/mlops/drift-detection`: grounded in the Deep-ML PSI drift detection title.
- `modules/ml/llm/beam-search`: exact Deep-ML title match for decoding.
- `modules/ml/llm/top-p-sampling`: exact Deep-ML title match for nucleus sampling.
- `modules/ml/llm/temperature-sampling`: exact Deep-ML title match for sampling control.
- `modules/ml/representation/contrastive-loss`: exact Deep-ML title match for SimCLR-style objectives.
- `modules/ml/reinforcement-learning/eligibility-traces`: grounded in the Deep-ML TD(llama) title.
- `modules/ml/systems/expert-load-balancing`: inferred MoE systems gap beyond pure routing and dispatch.

## Second Wave After That

- `modules/ml/evaluation/bootstrap-intervals`
- `modules/ml/optimization/warmup-cosine-decay`
- `modules/ml/llm/tokenizer-comparison`
- `modules/ml/reinforcement-learning/importance-sampling`
- `modules/ml/llm/top-k-sampling`
- `modules/ml/data/missing-indicator`
- `modules/ml/evaluation/permutation-test`
- `modules/ml/evaluation/isotonic-calibration`
- `modules/ml/llm/reranker-metrics`
- `modules/ml/mlops/request-sla`
