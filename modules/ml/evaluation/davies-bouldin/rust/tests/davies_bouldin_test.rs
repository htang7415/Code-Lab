use ml_evaluation_davies_bouldin::davies_bouldin;

#[test]
fn test_davies_bouldin() {
    assert!((davies_bouldin(0.5, 0.5, 2.0) - 0.5).abs() < 1e-6);
}
