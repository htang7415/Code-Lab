# Contributing

## Naming rules

- **Directories**: kebab-case (`prefix-sum`, `two-sum`, `binary-search`)
- **Python files**: snake_case (`prefix_sum.py`, `test_prefix_sum.py`)
- **Rust crates**: kebab-case directory, standard Rust naming inside

## Adding a module

A module teaches one concept with runnable code and tests.

```bash
./scripts/new_module.sh <track> <topic> <slug>
# Example: ./scripts/new_module.sh ml llm positional-encoding
```

This creates:

```
modules/<track>/<topic>/<slug>/
  README.md
  python/<slug_underscored>.py
  python/test_<slug_underscored>.py
```

Fill in the README with a concise explanation, implement the code, and write tests.

## Adding a problem

A problem is a practice exercise with a statement, solution, and tests.

```bash
./scripts/new_problem.sh <track> <topic> <slug>
# Example: ./scripts/new_problem.sh dsa arrays three-sum
```

This creates:

```
problems/<track>/<topic>/<slug>/
  meta.json
  problem.md
  python/solution.py
  python/test_solution.py
  rust/Cargo.toml
  rust/src/lib.rs
  rust/tests/solution_test.rs
```

### meta.json schema

Every problem must have a `meta.json`:

```json
{
  "id": "<track>-<topic>-<slug>",
  "slug": "<slug>",
  "title": "Human Readable Title",
  "track": "<track>",
  "topic": "<topic>",
  "difficulty": "easy | medium | hard",
  "tags": ["relevant", "tags"],
  "languages": ["python", "rust"]
}
```

## Testing

Run tests **one module or problem at a time**:

```bash
# Python
pytest modules/<track>/<topic>/<slug>/python -q
pytest problems/<track>/<topic>/<slug>/python -q

# Rust
cargo test --manifest-path problems/<track>/<topic>/<slug>/rust/Cargo.toml
```

Use the Makefile shortcuts:

```bash
make run-py PATH=modules/dsa/arrays/prefix-sum/python
make run-rust MANIFEST=problems/dsa/arrays/two-sum/rust/Cargo.toml
```

## Code style

- Keep code minimal and readable
- Add concise comments only where logic is not self-evident
- Each module/problem should be self-contained
