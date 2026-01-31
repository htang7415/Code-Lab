use ml_optimization_lr_cosine_decay::cosine_decay;

#[test]
fn test_cosine_decay_end() {
    assert!(cosine_decay(1.0, 10, 10).abs() < 1e-6);
}
