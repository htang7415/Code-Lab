use ml_models_adaboost::update_weights;

#[test]
fn test_update_weights() {
    let out = update_weights(&[0.5, 0.5], &[1, 0], 0.7);
    let sum: f64 = out.iter().sum();
    assert!((sum - 1.0).abs() < 1e-6);
}
