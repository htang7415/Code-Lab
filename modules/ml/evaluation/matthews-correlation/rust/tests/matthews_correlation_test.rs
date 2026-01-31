use ml_evaluation_matthews_correlation::mcc;

#[test]
fn test_mcc() {
    assert!((mcc(1, 1, 0, 0) - 1.0).abs() < 1e-6);
}
