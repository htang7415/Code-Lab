use ml_deep_learning_backpropagation::linear_backprop;

#[test]
fn test_linear_backprop() {
    let grad = linear_backprop(3.0, 0.5);
    assert_eq!(grad, 1.5);
}
