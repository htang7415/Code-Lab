use ml_deep_learning_automatic_differentiation::forward_grad;

#[test]
fn test_forward_grad() {
    assert_eq!(forward_grad(3.0), 6.0);
}
