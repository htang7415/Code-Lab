use ml_deep_learning_he_initialization::he_normal;

#[test]
fn test_he_length() {
    let weights = he_normal(2, 3, 1);
    assert_eq!(weights.len(), 6);
}
