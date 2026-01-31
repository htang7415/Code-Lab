use ml_fundamentals_gradient_descent::gd_step;

#[test]
fn test_gd_step() {
    assert!((gd_step(1.0, 0.5, 0.1) - 0.95).abs() < 1e-6);
}
