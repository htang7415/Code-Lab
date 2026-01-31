use ml_deep_learning_layernorm::layernorm;

#[test]
fn test_layernorm_mean() {
    let out = layernorm(&[1.0, 2.0, 3.0], 1e-5);
    let sum: f64 = out.iter().sum();
    assert!(sum.abs() < 1e-6);
}
