use ml_data_polynomial_features::poly_features;

#[test]
fn test_poly_features() {
    assert_eq!(poly_features(2.0, 3), vec![2.0, 4.0, 8.0]);
}
