use ml_deep_learning_rmsnorm::rmsnorm;

#[test]
fn test_rmsnorm_rms() {
    let out = rmsnorm(&[3.0, 4.0], 1e-5);
    let rms = (out.iter().map(|v| v * v).sum::<f64>() / out.len() as f64).sqrt();
    assert!((rms - 1.0).abs() < 1e-6);
}
