use ml_deep_learning_early_stopping::should_stop;

#[test]
fn test_should_stop() {
    let losses = vec![1.0, 0.9, 0.91, 0.92];
    assert!(should_stop(&losses, 2));
}
