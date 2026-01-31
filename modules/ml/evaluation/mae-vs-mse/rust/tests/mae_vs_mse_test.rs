use ml_evaluation_mae_vs_mse::mae_mse;

#[test]
fn test_mae_mse() {
    let (mae, mse) = mae_mse(&[1.0, 2.0], &[1.0, 3.0]);
    assert!((mae - 0.5).abs() < 1e-6);
    assert!((mse - 0.5).abs() < 1e-6);
}
