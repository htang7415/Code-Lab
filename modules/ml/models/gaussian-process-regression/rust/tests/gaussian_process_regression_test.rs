use ml_models_gaussian_process_regression::rbf_kernel;

#[test]
fn test_rbf_kernel() {
    assert!((rbf_kernel(&[0.0], &[0.0], 1.0) - 1.0).abs() < 1e-6);
}
