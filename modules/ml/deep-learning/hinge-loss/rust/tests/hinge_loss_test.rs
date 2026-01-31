use ml_deep_learning_hinge_loss::hinge_loss;

#[test]
fn test_hinge_loss() {
    assert_eq!(hinge_loss(2.0, 1), 0.0);
    assert_eq!(hinge_loss(0.2, 1), 0.8);
}
