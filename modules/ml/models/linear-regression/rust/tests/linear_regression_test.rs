use ml_models_linear_regression::predict;

#[test]
fn test_predict() {
    assert_eq!(predict(&[1.0, 2.0], &[0.5, 1.0], 0.0), 2.5);
}
