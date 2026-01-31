use ml_data_data_leakage::has_leakage;

#[test]
fn test_has_leakage() {
    assert!(has_leakage(&[1, 2], &[2, 3]));
}
