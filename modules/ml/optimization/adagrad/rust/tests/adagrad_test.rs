use ml_optimization_adagrad::adagrad_step;

#[test]
fn test_adagrad_step() {
    let (w, g2) = adagrad_step(1.0, 1.0, 0.0, 0.1, 1e-8);
    assert!(w < 1.0);
    assert!(g2 > 0.0);
}
