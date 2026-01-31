use ml_deep_learning_batchnorm_transformers::batch_stats;

#[test]
fn test_batch_stats() {
    let (mean, var) = batch_stats(&[vec![1.0, 2.0], vec![3.0, 4.0]]);
    assert_eq!(mean, 2.5);
    assert!(var > 0.0);
}
