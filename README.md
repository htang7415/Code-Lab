# Code Lab

Coding review and practice for machine learning, data structures & algorithms, AI agents, databases, and software engineering.

## Repo structure

```
code-lab/
  docs/          # Concept notes (markdown)
  modules/       # Concept labs — teach one idea with code + tests
  problems/      # Practice problems (LeetCode / deep-ml style)
  templates/     # Scaffolds for new modules and problems
  scripts/       # Helper scripts
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
make run-py TARGET=modules/dsa/arrays/prefix-sum/python
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

The `web/` directory contains a Next.js app. See [web/README.md](web/README.md) for setup and Vercel deployment instructions.

## License

[MIT](LICENSE)
