use ml_fundamentals_beta_binomial::beta_posterior;

#[test]
fn test_beta_posterior() {
    assert_eq!(beta_posterior(1.0, 1.0, 3, 2), (4.0, 3.0));
}
