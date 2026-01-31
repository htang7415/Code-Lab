use ml_evaluation_precision_recall::precision_recall;

#[test]
fn test_precision_recall() {
    let (p, r) = precision_recall(&[1, 0, 1], &[1, 1, 0]);
    assert!((p - 0.5).abs() < 1e-6);
    assert!((r - 0.5).abs() < 1e-6);
}
