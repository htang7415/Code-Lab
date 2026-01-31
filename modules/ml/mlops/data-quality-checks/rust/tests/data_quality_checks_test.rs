use ml_mlops_data_quality_checks::missing_rate;

#[test]
fn test_missing_rate() {
    let values = vec![Some(1.0), None, Some(2.0)];
    assert!((missing_rate(&values) - 1.0 / 3.0).abs() < 1e-6);
}
