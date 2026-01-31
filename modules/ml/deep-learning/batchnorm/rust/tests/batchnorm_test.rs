use ml_deep_learning_batchnorm::batchnorm;

#[test]
fn test_batchnorm_mean() {
    let out = batchnorm(&[1.0, 2.0, 3.0], 1e-5);
    let sum: f64 = out.iter().sum();
    assert!(sum.abs() < 1e-6);
}
