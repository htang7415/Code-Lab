use ml_systems_zero_gradients::zero_grad;

#[test]
fn test_zero_grad() {
    assert_eq!(zero_grad(&[1.0, -1.0]), vec![0.0, 0.0]);
}
