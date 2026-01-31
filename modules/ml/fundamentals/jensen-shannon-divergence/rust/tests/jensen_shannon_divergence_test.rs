use ml_fundamentals_jensen_shannon_divergence::js;

#[test]
fn test_js() {
    assert!((js(&[0.5, 0.5], &[0.5, 0.5]) - 0.0).abs() < 1e-6);
}
