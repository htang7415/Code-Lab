use ml_fundamentals_distributions::normalize_probs;

#[test]
fn test_normalize_probs() {
    let probs = normalize_probs(&[1.0, 1.0]);
    let sum: f64 = probs.iter().sum();
    assert!((sum - 1.0).abs() < 1e-6);
}
