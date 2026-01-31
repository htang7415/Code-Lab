use ml_deep_learning_l2_regularization::l2_penalty;

#[test]
fn test_l2_penalty() {
    assert!((l2_penalty(&[1.0, -2.0], 0.1) - 0.5).abs() < 1e-6);
}
