use ml_deep_learning_instancenorm::instancenorm;

#[test]
fn test_instancenorm_mean() {
    let out = instancenorm(&[1.0, 2.0, 3.0], 1e-5);
    let sum: f64 = out.iter().sum();
    assert!(sum.abs() < 1e-6);
}
