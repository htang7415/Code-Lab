use ml_evaluation_calinski_harabasz::calinski_harabasz;

#[test]
fn test_calinski_harabasz() {
    assert!((calinski_harabasz(10.0, 5.0, 2, 10) - 20.0).abs() < 1e-6);
}
