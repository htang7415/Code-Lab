use ml_deep_learning_focal_loss::focal_loss;

#[test]
fn test_focal_loss() {
    assert!(focal_loss(0.9, 2.0) < focal_loss(0.6, 2.0));
}
