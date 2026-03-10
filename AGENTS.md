# Code Lab — AGENTS.md

## What this repo is
Code Lab is a learning-first repo with:
- `docs/`  : concise concept notes (website-ready)
- `modules/`: compact learning modules with code and focused tests
- `web/`   : TypeScript Next.js site that renders repo content (Vercel deploy)

## Non-negotiable workflow
- **Run tests one module at a time.** Do NOT default to “run all tests”.
- Prefer **small, incremental edits** and keep everything easy to learn.
- Keep **structure and naming consistent** so content can be indexed for the website.

## Folder conventions
- Folder names: **kebab-case** (e.g., `prefix-sum`, `attention-causal`)
- Python files: **snake_case.py**

### Module layout
```
modules/<track>/<subtopic>/<slug>/
  README.md
  python/<name>.py
  python/test_<name>.py
  rust/ (optional)
    Cargo.toml
    src/lib.rs
    tests/<name>_test.rs
```

## How to run (one target)
### Python
Run pytest in the target folder:
```bash
pytest modules/<...>/python -q
```

### Rust
Run cargo test for the single crate:
```bash
cargo test --manifest-path modules/<...>/rust/Cargo.toml
```

### Web (Next.js)
```bash
cd web
pnpm install
pnpm --filter @codelab/site dev
```

## Adding new content
### Add a module (concept lab)
- Goal: teach **one** idea (short README + minimal code + tiny test).
- Use the repo template/script if available, otherwise copy an existing module and rename.

### ML authoring policy
- For the `ml` track, prefer **one coherent learning unit** over overly fragmented one-formula modules.
- A good ML module may cover a **concept family** when people naturally learn the ideas together.
  Examples: activation functions, normalization methods, decoding methods, calibration metrics.
- Keep separate modules only when the mental model, implementation pattern, or failure mode is clearly different.
  Examples: PCA, GMM-EM, backpropagation, PPO, KV cache.
- Do **not** create a new ML module for a narrow metric or variant if it adds little intuition beyond an existing family module.
- Dense ML modules are encouraged when they stay easy to scan. A strong ML module usually includes:
  - a short concept overview
  - grouped formulas or a comparison table
  - failure modes or trade-offs
  - compact code covering the family
  - one focused test file for the family
- Use `docs/` to provide the system map and comparisons. Use `modules/` to provide the smallest **useful** learning unit, which may be larger than a single formula.
- If consolidating existing ML modules, preserve URL stability. Prefer redirects or compatibility handling over breaking slugs.

## Website sync rule
- The website should NOT duplicate source content.
- If a change affects URL stability, prefer adding redirects rather than renaming slugs.

## Editing guidelines
- Keep docs short and correct.
- Avoid new dependencies unless clearly necessary.
- Prefer clarity over clever optimizations.
