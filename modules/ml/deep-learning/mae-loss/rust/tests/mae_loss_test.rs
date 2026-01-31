use ml_deep_learning_mae_loss::mae;

#[test]
fn test_mae() {
    assert!((mae(&[1.0, 2.0], &[1.0, 3.0]) - 0.5).abs() < 1e-6);
}
