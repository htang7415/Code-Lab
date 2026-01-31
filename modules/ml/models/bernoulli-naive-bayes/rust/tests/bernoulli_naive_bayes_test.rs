use ml_models_bernoulli_naive_bayes::bernoulli_log_likelihood;

#[test]
fn test_bernoulli_log_likelihood() {
    let ll = bernoulli_log_likelihood(&[1, 0], &[0.8, 0.2]);
    assert!(ll > -1.0);
}
