use ml_deep_learning_activations_relu_family::relu_family;

#[test]
fn test_relu_family() {
    let (relu, leaky, _, _) = relu_family(-2.0, 0.1);
    assert_eq!(relu, 0.0);
    assert!(leaky < 0.0);
}
