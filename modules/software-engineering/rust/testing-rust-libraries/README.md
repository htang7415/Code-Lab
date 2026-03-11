# Testing Rust Libraries

> Track: `software-engineering` | Topic: `rust`

## Concept

Rust libraries are easiest to test when most logic is pure, boundaries are injectable, and the crate exposes small deterministic functions.

## Key Points

- Pure functions are cheap to unit test.
- Hidden global state makes libraries harder to reason about and harder to isolate.
- Integration tests are strongest when the library surface is already clean.

## Minimal Code Mental Model

```rust
assert_eq!(normalize_slug("Hello, Rust!"), "hello-rust");
assert_eq!(test_scope(true, false), "integration");
assert!(library_ready_for_unit_tests(0, 1));
```

## Function

```rust
pub fn normalize_slug(input: &str) -> String;
pub fn test_scope(has_io: bool, pure_logic: bool) -> &'static str;
pub fn library_ready_for_unit_tests(hidden_globals: usize, injectable_boundaries: usize) -> bool;
```

## Run tests

```bash
cargo test --manifest-path modules/software-engineering/rust/testing-rust-libraries/rust/Cargo.toml
```
