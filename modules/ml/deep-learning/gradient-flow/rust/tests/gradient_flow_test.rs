use ml_deep_learning_gradient_flow::propagate_variance;

#[test]
fn test_propagate_variance() {
    assert_eq!(propagate_variance(1.0, &[0.5, 2.0]), 1.0);
}
