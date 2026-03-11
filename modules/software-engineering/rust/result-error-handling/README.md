# Result Error Handling

> Track: `software-engineering` | Topic: `rust`

## Concept

Rust error handling is strongest when failures are explicit in the type system and callers are forced to deal with them instead of relying on hidden exceptions.

## Key Points

- `Result` makes success and failure part of the function signature.
- Small, explicit error enums are easier to test and reason about.
- Propagating errors with `?` keeps code linear without hiding control flow.

## Minimal Code Mental Model

```rust
let port = parse_port("8080")?;
let addr = bind_address("127.0.0.1", "8080")?;
```

## Function

```rust
pub enum ParsePortError {
    Empty,
    Invalid,
    OutOfRange,
    InvalidHost,
}

pub fn parse_port(input: &str) -> Result<u16, ParsePortError>;
pub fn bind_address(host: &str, port: &str) -> Result<String, ParsePortError>;
```

## Run tests

```bash
cargo test --manifest-path modules/software-engineering/rust/result-error-handling/rust/Cargo.toml
```
