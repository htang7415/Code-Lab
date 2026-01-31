use ml_optimization_nesterov::nesterov_step;

#[test]
fn test_nesterov_step() {
    let (w, v) = nesterov_step(1.0, 1.0, 0.0, 0.1, 0.9);
    assert!(w < 1.0);
    assert_eq!(v, 1.0);
}
