use ml_reinforcement_learning_return_discount::discounted_return;

#[test]
fn test_discounted_return() {
    assert!((discounted_return(&[1.0, 1.0], 0.5) - 1.5).abs() < 1e-6);
}
