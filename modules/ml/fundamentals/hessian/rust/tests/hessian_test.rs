use ml_fundamentals_hessian::hessian_quadratic;

#[test]
fn test_hessian_quadratic() {
    assert_eq!(hessian_quadratic(3.0), 6.0);
}
