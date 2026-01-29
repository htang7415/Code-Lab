# Code Lab

Learn by building: short notes, runnable mini-labs, and practice problems
across DSA, ML (LLM/RL), AI agents, databases, and software engineering.

Code Lab is designed for daily practice: one idea at a time, one test target
at a time, with clear structure so content can scale without confusion.

## Why Code Lab

- Learn an idea, then run it immediately with a tiny test
- Keep concepts and exercises separate but linked
- Use Python by default, with Rust encouraged
- Make content website-ready from day one

## Repo map

```
code-lab/
  docs/          # Concept notes (website-ready)
  modules/       # Concept labs — one idea + minimal code + tiny test
  problems/      # Practice problems (LeetCode / deep-ml style)
  templates/     # Scaffolds for new modules/problems
  scripts/       # Helper scripts (one-by-one tests, scaffolding)
  web/           # Next.js website (TypeScript, Vercel-deployable)
```

## Tracks

| Track | Path prefix |
|-------|-------------|
| Data Structures & Algorithms | `dsa/` |
| Machine Learning (incl. LLM, RL) | `ml/` |
| AI Agents | `ai-agents/` |
| Databases | `databases/` |
| Software Engineering | `software-engineering/` |

## Learning flow

1. Read a concept note in `docs/`
2. Run a related module test in `modules/`
3. Solve a practice problem in `problems/`

## Quick start

### Prerequisites

- Python 3.10+ with `pytest`
- Rust toolchain (`cargo`) — needed only for Rust solutions
- Node.js 18+ and `pnpm` — needed only for the website

### Install Python dependencies

```bash
pip install -e ".[dev]"
```

For ML modules (numpy-based), also install:

```bash
pip install -e ".[dev,ml]"
```

### Run a single module's tests

```bash
pytest modules/dsa/arrays/prefix-sum/python -q
```

### Run a single problem's tests

```bash
pytest problems/dsa/arrays/two-sum/python -q
```

### Run a Rust crate's tests

```bash
cargo test --manifest-path problems/dsa/arrays/two-sum/rust/Cargo.toml
```

### Using the Makefile

```bash
make run-py PATH=modules/dsa/arrays/prefix-sum/python
make run-rust MANIFEST=problems/dsa/arrays/two-sum/rust/Cargo.toml
```

## Scaffold new content

```bash
# New module
./scripts/new_module.sh dsa arrays sliding-window

# New problem
./scripts/new_problem.sh dsa arrays three-sum
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for naming rules and testing conventions.

## Website

The `web/` directory contains a Next.js app. See [web/README.md](web/README.md)
for setup and Vercel deployment instructions.

## Inspiration

The structure and learning-first approach are inspired by standout learning
repositories on GitHub, including
[The Algorithms](https://github.com/TheAlgorithms) and
[OpenAI Cookbook](https://github.com/openai/openai-cookbook).

## License

[MIT](LICENSE)
