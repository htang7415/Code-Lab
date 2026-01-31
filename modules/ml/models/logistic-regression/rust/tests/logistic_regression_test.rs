use ml_models_logistic_regression::predict_proba;

#[test]
fn test_predict_proba() {
    let p = predict_proba(&[0.0], &[1.0], 0.0);
    assert!((p - 0.5).abs() < 1e-6);
}
