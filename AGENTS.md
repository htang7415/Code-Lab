# Code Lab — AGENTS.md

## What this repo is
Code Lab is a learning-first repo with:
- `docs/`  : concise concept notes (website-ready)
- `modules/`: small concept labs (one idea + minimal code + a tiny test)
- `web/`   : TypeScript Next.js site that renders repo content (Vercel deploy)

## Non-negotiable workflow
- **Run tests one module/problem at a time.** Do NOT default to “run all tests”.
- Prefer **small, incremental edits** and keep everything easy to learn.
- Keep **structure and naming consistent** so content can be indexed for the website.

## Folder conventions
- Folder names: **kebab-case** (e.g., `prefix-sum`, `attention-causal`)
- Python files: **snake_case.py**
- Each problem must include `meta.json` + `problem.md`.

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

#### Required `meta.json` keys
```json
{
  "id": "dsa-arrays-two-sum",
  "slug": "two-sum",
  "title": "Two Sum",
  "track": "dsa",
  "topic": "arrays",
  "difficulty": "easy",
  "tags": ["hashmap"],
  "languages": ["python", "rust"]
}
```

## Website sync rule
- The website should NOT duplicate source content.
- If a change affects URL stability, prefer adding redirects rather than renaming slugs.

## Editing guidelines
- Keep docs short and correct.
- Avoid new dependencies unless clearly necessary.
- Prefer clarity over clever optimizations.
