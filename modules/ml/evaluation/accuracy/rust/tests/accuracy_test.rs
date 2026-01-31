use ml_evaluation_accuracy::accuracy;

#[test]
fn test_accuracy() {
    assert!((accuracy(&[1, 0, 1], &[1, 1, 1]) - 2.0 / 3.0).abs() < 1e-6);
}
