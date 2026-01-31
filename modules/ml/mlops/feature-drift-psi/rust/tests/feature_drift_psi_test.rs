use ml_mlops_feature_drift_psi::psi;

#[test]
fn test_psi_zero() {
    assert!(psi(&[0.5, 0.5], &[0.5, 0.5]).abs() < 1e-6);
}
