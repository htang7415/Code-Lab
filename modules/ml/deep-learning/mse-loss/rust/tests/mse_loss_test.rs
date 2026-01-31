use ml_deep_learning_mse_loss::mse;

#[test]
fn test_mse() {
    assert!((mse(&[1.0, 2.0], &[1.0, 3.0]) - 0.5).abs() < 1e-6);
}
