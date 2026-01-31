use ml_optimization_detect_nans::has_nan;

#[test]
fn test_has_nan() {
    let values = vec![0.0, f64::NAN];
    assert!(has_nan(&values));
}
