use ml_models_decision_trees::gini_impurity;

#[test]
fn test_gini_impurity() {
    assert!((gini_impurity(&[0, 0, 1, 1]) - 0.5).abs() < 1e-6);
}
