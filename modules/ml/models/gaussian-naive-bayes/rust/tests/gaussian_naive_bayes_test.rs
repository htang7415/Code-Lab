use ml_models_gaussian_naive_bayes::gaussian_log_likelihood;

#[test]
fn test_gaussian_log_likelihood() {
    let ll = gaussian_log_likelihood(&[0.0], &[0.0], &[1.0]);
    assert!(ll < 0.0);
}
