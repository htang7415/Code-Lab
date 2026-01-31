use ml_deep_learning_knowledge_distillation_loss::distill_loss;

#[test]
fn test_distill_loss() {
    let loss = distill_loss(&[2.0, 0.0], &[2.0, 0.0], 1.0);
    assert!(loss < 1e-6);
}
