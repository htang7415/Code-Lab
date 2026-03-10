# Machine Learning

Use this track to learn the ML stack from first principles without getting buried in old or low-value variants.
The default goal is not exhaustive coverage. It is fast, deep understanding of the concepts that matter most for modern AI work in 2026.

## How To Use This Track

- Start with one study path, not the whole tree.
- Use section docs for the concept map and canonical modules for the main learning unit.
- Use narrow modules only after the canonical family makes sense.
- Treat `artifacts/deepml/problem_titles.md` as the main scope boundary for ML coverage.

## Study Paths

- Beginner path (`docs/ml/path-beginner`)
- Interview path (`docs/ml/path-interview`)
- LLM systems path (`docs/ml/path-llm-systems`)
- Math-first path (`docs/ml/path-math-first`)

## Learning Order

- Math and foundations (`docs/ml/fundamentals`)
- Data and preprocessing (`docs/ml/data`)
- Models and evaluation (`docs/ml/models`, `docs/ml/evaluation`)
- Deep learning and optimization (`docs/ml/deep-learning`, `docs/ml/optimization`)
- LLMs and modern NLP (`docs/ml/llm`)
- Systems, MLOps, RL, and vision (`docs/ml/systems`, `docs/ml/mlops`, `docs/ml/reinforcement-learning`, `docs/ml/computer-vision`)

## Canonical Families

- Deep learning: `activation-functions`, `normalization-methods`
- Evaluation: `calibration-metrics`, `uncertainty-intervals`, `ranking-metrics`, `classification-metrics-core`, `agreement-metrics`, `binary-rate-comparison-metrics`
- LLM: `decoding-methods`, `retrieval-metrics`
- Data: `scaling-methods`, `categorical-encoding-methods`, `sparse-text-feature-methods`, `structured-feature-methods`

## Writing Standard

- Keep docs short, teachable, and current.
- Prefer first-principles explanation plus a little math and code over long catalogs.
- Prefer canonical concepts over many near-duplicate calculators.
- Only add topics outside `problem_titles.md` when they are clearly important to AI practice in 2026.

## Near-Term Priority

- Keep heavy pages concise and family-first.
- Rebalance underrepresented areas such as representation, diffusion, and RL-for-LLM.
- Use `docs/ml/roadmap` for coverage audits instead of title-by-title expansion.
