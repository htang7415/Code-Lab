use ml_deep_learning_activations_softmax_softplus_softsign::{softmax, softplus, softsign};

#[test]
fn test_softmax_sum() {
    let row = softmax(&[1.0, 1.0]);
    let sum: f64 = row.iter().sum();
    assert!((sum - 1.0).abs() < 1e-6);
    assert!(softplus(0.0) > 0.0);
    assert!((softsign(1.0) - 0.5).abs() < 1e-6);
}
