use ml_models_softmax_regression::softmax;

#[test]
fn test_softmax_sum() {
    let sum: f64 = softmax(&[1.0, 1.0]).iter().sum();
    assert!((sum - 1.0).abs() < 1e-6);
}
