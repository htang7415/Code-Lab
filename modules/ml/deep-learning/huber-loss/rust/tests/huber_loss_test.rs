use ml_deep_learning_huber_loss::huber;

#[test]
fn test_huber() {
    assert!((huber(1.0, 0.0, 1.0) - 0.5).abs() < 1e-6);
}
