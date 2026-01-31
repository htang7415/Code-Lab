use ml_deep_learning_weight_decay::weight_decay_step;

#[test]
fn test_weight_decay_step() {
    assert!((weight_decay_step(1.0, 0.0, 0.1, 0.1) - 0.99).abs() < 1e-6);
}
