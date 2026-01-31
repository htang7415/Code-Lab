use ml_mlops_etl_pipeline::normalize;

#[test]
fn test_normalize_mean() {
    let out = normalize(&[1.0, 2.0, 3.0]);
    let sum: f64 = out.iter().sum();
    assert!(sum.abs() < 1e-6);
}
