use ml_fundamentals_convex_vs_nonconvex::is_convex_quadratic;

#[test]
fn test_is_convex_quadratic() {
    assert!(is_convex_quadratic(1.0));
    assert!(!is_convex_quadratic(-1.0));
}
