use ml_deep_learning_l1_regularization::l1_penalty;

#[test]
fn test_l1_penalty() {
    assert!((l1_penalty(&[1.0, -2.0], 0.1) - 0.3).abs() < 1e-6);
}
