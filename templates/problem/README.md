# {{SLUG}}

> Track: `{{TRACK}}` | Topic: `{{TOPIC}}` | ID: `{{ID}}`

## Summary

<!-- Add a short overview or notes about the problem. -->

## Files

- `problem.md`: statement and examples
- `python/solution.py`: reference solution
- `python/test_solution.py`: tests
- `rust/` (optional): Rust solution and tests

## Run tests

```bash
pytest problems/{{TRACK}}/{{TOPIC}}/{{SLUG}}/python -q
cargo test --manifest-path problems/{{TRACK}}/{{TOPIC}}/{{SLUG}}/rust/Cargo.toml
```
