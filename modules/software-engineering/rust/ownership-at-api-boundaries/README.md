# Ownership At API Boundaries

> Track: `software-engineering` | Topic: `rust`

## Concept

Rust ownership becomes most useful at API boundaries because it makes borrowing, mutation, and consumption explicit to the caller.

## Key Points

- Borrowing lets callers inspect data without giving up ownership.
- Mutable borrowing makes in-place updates explicit.
- Consuming ownership is a signal that the API takes responsibility for the value.

## Minimal Code Mental Model

```rust
let mut doc = Document::new("draft", "body");
assert_eq!(title_len(&doc), 5);
rename(&mut doc, "final");
let title = take_title(doc);
```

## Function

```rust
pub struct Document {
    pub title: String,
    pub body: String,
}

pub fn title_len(doc: &Document) -> usize;
pub fn rename(doc: &mut Document, new_title: &str);
pub fn take_title(doc: Document) -> String;
```

## Run tests

```bash
cargo test --manifest-path modules/software-engineering/rust/ownership-at-api-boundaries/rust/Cargo.toml
```
