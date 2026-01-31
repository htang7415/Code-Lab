use ml_fundamentals_jacobian::jacobian;

fn f1(x: f64, y: f64) -> f64 { x + y }
fn f2(x: f64, y: f64) -> f64 { x * y }

#[test]
fn test_jacobian() {
    let j = jacobian(f1, f2, 2.0, 3.0, 1e-5);
    assert!((j[0][0] - 1.0).abs() < 1e-3);
    assert!((j[1][0] - 3.0).abs() < 1e-3);
}
