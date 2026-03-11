use software_engineering_rust_async_rust_services::{
    async_service_fit, backpressure_needed, block_on_ready, concurrency_budget,
};

#[test]
fn test_async_service_fit_prefers_io_bound_workloads() {
    assert!(async_service_fit(120, 20));
    assert!(!async_service_fit(20, 120));
}

#[test]
fn test_concurrency_budget_is_available_from_ready_async_function() {
    let budget = block_on_ready(concurrency_budget(4, 25));
    assert_eq!(budget, 100);
}

#[test]
fn test_backpressure_needed_when_in_flight_exceeds_budget() {
    assert!(backpressure_needed(120, 100));
    assert!(!backpressure_needed(80, 100));
}
