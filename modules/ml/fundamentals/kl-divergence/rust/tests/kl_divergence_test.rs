use ml_fundamentals_kl_divergence::kl;

#[test]
fn test_kl() {
    assert!(kl(&[0.5, 0.5], &[0.5, 0.5]).abs() < 1e-6);
}
