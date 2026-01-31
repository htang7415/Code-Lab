use ml_evaluation_roc_auc::auc;

#[test]
fn test_auc() {
    assert!((auc(&[0.0, 1.0], &[0.0, 1.0]) - 0.5).abs() < 1e-6);
}
