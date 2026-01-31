use ml_optimization_sgd::sgd_step;

#[test]
fn test_sgd_step() {
    assert!((sgd_step(1.0, 0.5, 0.1) - 0.95).abs() < 1e-6);
}
