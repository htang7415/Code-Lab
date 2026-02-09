use ml_deep_learning_automatic_differentiation::Value;

#[test]
fn test_value_mul_add_relu_backward() {
    let a = Value::new(2.0);
    let b = Value::new(-3.0);
    let c = Value::new(10.0);
    let out = a.mul(&b).add(&c).relu();
    out.backward();

    assert!((out.data() - 4.0).abs() < 1e-12);
    assert!((a.grad() - (-3.0)).abs() < 1e-12);
    assert!((b.grad() - 2.0).abs() < 1e-12);
    assert!((c.grad() - 1.0).abs() < 1e-12);
}

#[test]
fn test_value_zero_grad_single_node() {
    let x = Value::new(3.0);
    let two = Value::new(2.0);
    let y = x.mul(&two);
    y.backward();
    assert!((x.grad() - 2.0).abs() < 1e-12);
    x.zero_grad();
    assert!((x.grad() - 0.0).abs() < 1e-12);
}
