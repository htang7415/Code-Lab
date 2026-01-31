use ml_fundamentals_covariance::covariance;

#[test]
fn test_covariance() {
    assert!((covariance(&[1.0, 2.0], &[1.0, 2.0]) - 0.25).abs() < 1e-6);
}
