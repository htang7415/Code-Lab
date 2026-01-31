use ml_models_random_forest::bootstrap_indices;

#[test]
fn test_bootstrap_indices_len() {
    assert_eq!(bootstrap_indices(5, 1).len(), 5);
}
