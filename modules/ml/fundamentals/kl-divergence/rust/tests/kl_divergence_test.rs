use ml_fundamentals_kl_divergence::kl;

#[test]
fn test_kl_is_zero_for_matching_distributions() {
    assert!(kl(&[0.5, 0.5], &[0.5, 0.5]).abs() < 1e-6);
}

#[test]
fn test_kl_is_infinite_when_q_misses_positive_mass() {
    assert!(kl(&[1.0, 0.0], &[0.0, 1.0]).is_infinite());
}
