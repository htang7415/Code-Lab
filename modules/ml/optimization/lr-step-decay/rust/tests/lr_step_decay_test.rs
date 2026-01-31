use ml_optimization_lr_step_decay::step_decay;

#[test]
fn test_step_decay() {
    assert!((step_decay(0.1, 10, 0.5, 10) - 0.05).abs() < 1e-6);
}
