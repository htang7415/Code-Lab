use ml_deep_learning_vanishing_exploding_gradients::gradient_chain;

#[test]
fn test_gradient_chain() {
    assert_eq!(gradient_chain(&[0.5, 0.5], 1.0), 0.25);
}
