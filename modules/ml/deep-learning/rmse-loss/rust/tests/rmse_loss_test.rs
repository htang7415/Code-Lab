use ml_deep_learning_rmse_loss::rmse;

#[test]
fn test_rmse() {
    let val = rmse(&[1.0, 2.0], &[1.0, 3.0]);
    assert!((val - (0.5_f64).sqrt()).abs() < 1e-6);
}
