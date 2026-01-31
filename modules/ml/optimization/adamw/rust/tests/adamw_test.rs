use ml_optimization_adamw::adamw_step;

#[test]
fn test_adamw_step() {
    let (w, _, _) = adamw_step(1.0, 1.0, 0.0, 0.0, 0.1, 0.1, 0.9, 0.999, 1e-8);
    assert!(w < 1.0);
}
