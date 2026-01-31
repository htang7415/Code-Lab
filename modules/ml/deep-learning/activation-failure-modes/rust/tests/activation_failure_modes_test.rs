use ml_deep_learning_activation_failure_modes::dead_relu_fraction;

#[test]
fn test_dead_relu_fraction() {
    let frac = dead_relu_fraction(&[-1.0, 0.0, 2.0]);
    assert!((frac - 2.0 / 3.0).abs() < 1e-6);
}
