use ml_deep_learning_xavier_initialization::xavier_uniform;

#[test]
fn test_xavier_length() {
    let weights = xavier_uniform(2, 3, 1);
    assert_eq!(weights.len(), 6);
}
