use ml_mlops_prediction_monitoring::mean_shift;

#[test]
fn test_mean_shift() {
    assert_eq!(mean_shift(&[0.0, 0.0], &[1.0, 1.0]), 1.0);
}
