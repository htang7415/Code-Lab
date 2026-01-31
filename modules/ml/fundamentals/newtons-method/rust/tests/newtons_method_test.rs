use ml_fundamentals_newtons_method::newton_step;

#[test]
fn test_newton_step() {
    assert!((newton_step(1.0, 2.0, 4.0) - 0.5).abs() < 1e-6);
}
