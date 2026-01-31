use ml_deep_learning_gradient_checking::grad_check;

fn square(x: f64) -> f64 { x * x }

#[test]
fn test_grad_check_square() {
    let approx = grad_check(square, 3.0, 1e-5);
    assert!((approx - 6.0).abs() < 1e-3);
}
