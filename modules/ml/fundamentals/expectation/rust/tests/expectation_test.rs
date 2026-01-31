use ml_fundamentals_expectation::expectation;

#[test]
fn test_expectation() {
    assert!((expectation(&[0.0, 1.0], &[0.5, 0.5]) - 0.5).abs() < 1e-6);
}
