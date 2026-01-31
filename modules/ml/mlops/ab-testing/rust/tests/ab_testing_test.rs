use ml_mlops_ab_testing::conversion_rate;

#[test]
fn test_conversion_rate() {
    assert!((conversion_rate(50, 100) - 0.5).abs() < 1e-6);
}
