use ml_optimization_lr_exponential_decay::exp_decay;

#[test]
fn test_exp_decay() {
    assert!((exp_decay(0.1, 0.0, 10.0) - 0.1).abs() < 1e-6);
}
