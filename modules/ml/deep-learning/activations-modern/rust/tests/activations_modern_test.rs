use ml_deep_learning_activations_modern::modern_activations;

#[test]
fn test_modern_activations() {
    let (_, gelu, _, _) = modern_activations(1.0);
    assert!(gelu.is_finite());
}
