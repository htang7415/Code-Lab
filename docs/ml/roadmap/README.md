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

- `modules/ml/systems/context-parallelism`: covers long-context serving and communication trade-offs.
- `modules/ml/systems/tensor-parallelism`: covers shard-by-dimension compute and all-reduce costs.
- `modules/ml/systems/prefix-cache-metrics`: covers cache hit-rate reasoning and practical serving gains.
- `modules/ml/generative/ddpm-sampling`: adds the common reverse-sampling step that appears throughout diffusion curricula.
- `modules/ml/data/outlier-detection`: adds a practical preprocessing and anomaly-screening baseline.
- `modules/ml/models/lle`: adds a standard manifold learning baseline from the title list.
- `modules/ml/models/tsne-gradient`: covers the core optimization idea behind t-SNE.
- `modules/ml/models/bic-aic`: covers model selection for mixture-style models.
- `modules/ml/llm/exact-match`: adds normalized answer matching as a simple evaluation primitive.
- `modules/ml/llm/judge-pairwise`: adds judge-based comparison as a modern LLM eval pattern.

## Second Wave After That

- `modules/ml/systems/tensor-parallelism`
- `modules/ml/systems/context-parallelism`
- `modules/ml/systems/expert-parallelism`
- `modules/ml/generative/ddpm-sampling`
- `modules/ml/generative/classifier-free-guidance`
- `modules/ml/models/lle`
- `modules/ml/models/tsne-gradient`
- `modules/ml/models/bic-aic`
- `modules/ml/llm/exact-match`
- `modules/ml/llm/judge-pairwise`
