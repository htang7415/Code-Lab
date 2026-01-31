use ml_optimization_sgd_momentum::momentum_step;

#[test]
fn test_momentum_step() {
    let (w, v) = momentum_step(1.0, 1.0, 0.0, 0.1, 0.9);
    assert_eq!(w, 0.9);
    assert_eq!(v, 1.0);
}
