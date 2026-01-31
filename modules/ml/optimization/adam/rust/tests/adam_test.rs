use ml_optimization_adam::adam_step;

#[test]
fn test_adam_step() {
    let (w, m, v) = adam_step(1.0, 1.0, 0.0, 0.0, 0.1, 0.9, 0.999, 1e-8);
    assert!(w < 1.0);
    assert!(m > 0.0);
    assert!(v > 0.0);
}
