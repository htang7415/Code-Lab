# Traits And Abstraction Boundaries

> Track: `software-engineering` | Topic: `rust`

## Concept

Traits define the behavior a caller needs while letting implementations vary behind a narrow boundary.

## Key Points

- Traits are most useful when the boundary is stable and the implementations vary.
- Generic functions and trait objects solve related but different abstraction needs.
- Narrow traits are easier to test and reuse than broad “god interfaces.”

## Minimal Code Mental Model

```rust
let upper = UppercaseFormatter;
assert_eq!(render(&upper, "hi"), "HI");
```

## Function

```rust
pub trait Formatter {
    fn format(&self, input: &str) -> String;
}

pub fn render<F: Formatter>(formatter: &F, input: &str) -> String;
pub fn render_all(formatters: &[&dyn Formatter], input: &str) -> Vec<String>;
```

## Run tests

```bash
cargo test --manifest-path modules/software-engineering/rust/traits-and-abstraction-boundaries/rust/Cargo.toml
```
