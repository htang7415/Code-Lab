# Code Lab — Repo Generator Prompt (for Claude)

Use this prompt to generate the **first working version** of a GitHub repository named **`Code-Lab`**.

## 0) Role and goal
Act as a senior engineer and educator. Create a repo skeleton that supports:
- **Learning (concept notes + runnable mini-labs)**
- **Python + Rust** code (solutions/tests run locally)
- A future **TypeScript web site** (Next.js) deployable on **Vercel**
- Tests should be run **one module at a time** (not “run everything” by default).

The user will add more code later one by one for each topic. This first version must be clean, consistent, and easy to extend with several simple examples.

## 1) What to generate
Create the repository structure, starter docs, templates, and small example modules so that a newcomer can:
1) read a concept note,
2) run one module’s tests,
3) understand how to add more.

### 1.1 Top-level files (must include)
- `README.md` (clear overview + how to run a single module)
- `ROADMAP.md` (phases for growth + website plan)
- `CONTRIBUTING.md` (how to add modules, naming rules, testing rules)
- `LICENSE` (MIT)
- `.gitignore`
- `Makefile` (targets to run *one-by-one* tests; no global “test all” as the default)
- `scripts/` helper scripts (see below)
- `templates/` scaffolds (see below)

### 1.2 Topic coverage (create directories now, even if empty)
Create **both** `docs/` and `modules/` trees for these topics.

#### A) Data Structures & Algorithms (DSA)
Subtopics (directories):
- arrays, strings, linked-list, stack-queue, hashing, heap, sorting, binary-search, recursion
- trees, tries
- graphs, union-find, shortest-path, topo-sort
- greedy, backtracking
- dp (1d, 2d, knapsack, lis, interval)
- bit, math, intervals

#### B) Machine Learning (ML)
Subtopics (directories):
- fundamentals (math/prob/stats/metrics), data (splits/leakage/preprocessing)
- optimization (gd/sgd/momentum/adam/schedules/stability)
- models (linear/trees/mlp/cnn/rnn/transformer/gnn)
- deep-learning (init/norm/dropout/training loops)
- representation (embeddings/tokenization/features)
- generative (autoregressive/vae/diffusion)
- evaluation (cv/error analysis/calibration/uncertainty/robustness)
- mlops (packaging/logging/serving/monitoring/ci)
- systems (gpu/perf/distributed/profiling)

Add **LLM** and **Reinforcement Learning** as first-class areas:
- `llm/`: tokenization, embeddings, attention-transformer, pretraining-objectives, finetuning, alignment, inference-serving, evaluation
- `reinforcement-learning/`: bandits, mdp, dynamic-programming, model-free-value, policy-gradient, actor-critic, exploration, offline-rl, rl-for-llm

#### C) AI Agents
Subtopics:
- prompting, tool-use, planning, memory, rag, multi-agent, evals, guardrails, observability

#### D) Databases
Subtopics:
- relational, sql-patterns, schema-design, indexing, transactions, query-plans
- nosql, caching, streaming, vector-db

#### E) Software Engineering
Subtopics:
- python, rust, testing, tooling, performance, concurrency, design-patterns
- apis, system-design, security-basics

### 1.3 Repo layout (required)
Use this layout (you may add small improvements, but keep the idea):

```
code-lab/
  docs/
  modules/
  templates/
  scripts/
  web/
```

## 2) Conventions (important)
### 2.1 Naming
- Directory names: **kebab-case**
- Python modules: snake_case filenames
- Each module has a **stable slug**.

### 2.2 Testing philosophy (one-by-one)
Design commands so the learner runs a *single* module at a time:

Python examples:
- `pytest modules/dsa/arrays/prefix-sum/python -q`

Rust examples:
- `cargo test --manifest-path modules/dsa/arrays/prefix-sum/rust/Cargo.toml`

Do **not** make the default workflow “run all tests”. It’s okay to include an optional “test all” script, but it must not be the primary path.

## 3) Scripts to include
Create these scripts (POSIX shell; keep them simple and documented):
- `scripts/new_module.sh` — scaffold a new module from `templates/module`
- `scripts/run_py.sh <path>` — run pytest for one target folder path
- `scripts/run_rust.sh <path-to-Cargo.toml>` — run cargo test for one crate

Also include a minimal `Makefile` with targets:
- `make run-py PATH=...`
- `make run-rust MANIFEST=...`
- optional: `make lint` (python ruff optional), `make format` (optional)

## 4) Templates to include
Create `templates/module/` with placeholders:
- `README.md` template
- Python skeleton: `solution.py` + `test_solution.py` (or similarly named)
- Rust skeleton: `Cargo.toml`, `src/lib.rs`, `tests/...`

## 5) Web (TypeScript) setup now
Create `web/` as a pnpm workspace with a Next.js TypeScript app, clear and high tech style:
- `web/apps/site` (Next.js App Router, TypeScript)
- `web/packages/content-indexer` (a small TS script)

### 5.1 Content indexer requirement
Implement a script that scans:
- `../modules/**/README.md`
- `../docs/**/*.md`
and generates index files used by the site, e.g.:
- `web/apps/site/src/content/content_index.json`
- `web/apps/site/src/content/search_index.json`

It only needs to support listing docs and modules by track/topic.

### 5.2 Vercel deployment notes
In `web/README.md`, document how to deploy with Vercel:
- Root directory: `web`
- Build command: `pnpm --filter @codelab/site build`
- Install command: `pnpm install --frozen-lockfile`

## 6) Include small examples (must include)
Add at least these **ready-to-run** examples to demonstrate the pattern:

### 6.1 DSA module example (prefix sum)
- `modules/dsa/arrays/prefix-sum/`
  - `README.md`
  - `python/prefix_sum.py`
  - `python/test_prefix_sum.py`
  - (Rust version optional for v1)

### 6.2 ML LLM module example (causal attention mask)
- `modules/ml/llm/attention-causal/`
  - `README.md`
  - `python/attention.py`
  - `python/test_attention.py`

### 6.3 ML RL module example (epsilon-greedy bandit)
- `modules/ml/reinforcement-learning/bandit-epsilon-greedy/`
  - `README.md`
  - `python/bandit.py`
  - `python/test_bandit.py`

## 7) Python tooling (minimal)
Add `tooling/python/` or a root `pyproject.toml` (choose one) that sets up:
- `pytest` for tests
- optional `ruff` for lint (nice but not mandatory)
Keep instructions simple in `README.md`.

## 8) Output format (important)
If you are generating this in an environment that can create files, **create the files**.

If you must output in chat, format as a multi-file patch style with clear file paths, e.g.:

- `README.md`
  ```md
  ...
  ```
- `scripts/run_py.sh`
  ```bash
  ...
  ```

Do not omit file contents for required items.

## 9) Quality bar
- Keep docs concise but correct.
- Keep code minimal, readable, and tested with concise comments.
- Avoid over-engineering.
- Ensure all example modules run as documented.

---

## Final check before finishing
- Repo has all topic directories under `docs/` and `modules/`.
- Examples run one-by-one with commands shown in README.
- Next.js app builds, and the content-indexer script can generate index JSON from `docs/` + `modules/`.
