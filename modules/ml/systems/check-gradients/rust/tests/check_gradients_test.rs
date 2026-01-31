use ml_systems_check_gradients::gradients_ok;

#[test]
fn test_gradients_ok() {
    assert!(gradients_ok(&[0.0, 1.0]));
    assert!(!gradients_ok(&[0.0, 0.0]));
}
