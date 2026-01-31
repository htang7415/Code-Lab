use ml_optimization_rmsprop::rmsprop_step;

#[test]
fn test_rmsprop_step() {
    let (w, v) = rmsprop_step(1.0, 1.0, 0.0, 0.1, 0.9, 1e-8);
    assert!(w < 1.0);
    assert!(v > 0.0);
}
