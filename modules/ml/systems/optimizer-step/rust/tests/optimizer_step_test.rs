use ml_systems_optimizer_step::step;

#[test]
fn test_step() {
    assert!((step(1.0, 0.5, 0.1) - 0.95).abs() < 1e-6);
}
