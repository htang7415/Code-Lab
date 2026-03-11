# Async Rust Services

> Track: `software-engineering` | Topic: `rust`

## Concept

Async Rust services are most useful for I/O-bound concurrency, but they still need explicit concurrency limits and backpressure.

## Key Points

- Async in Rust helps when work waits on external operations more than it burns CPU.
- Concurrency budgets should stay explicit.
- Backpressure is a first-class service behavior, not an afterthought.

## Minimal Code Mental Model

```rust
let budget = block_on_ready(concurrency_budget(4, 25));
assert!(async_service_fit(120, 20));
assert!(backpressure_needed(120, budget));
```

## Function

```rust
pub async fn concurrency_budget(worker_count: usize, per_worker_in_flight: usize) -> usize;
pub fn async_service_fit(network_wait_ms: u64, cpu_ms: u64) -> bool;
pub fn backpressure_needed(in_flight: usize, budget: usize) -> bool;
pub fn block_on_ready<F: Future>(future: F) -> F::Output;
```

## Run tests

```bash
cargo test --manifest-path modules/software-engineering/rust/async-rust-services/rust/Cargo.toml
```
