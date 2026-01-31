use ml_evaluation_gini_impurity::gini;

#[test]
fn test_gini() {
    assert!((gini(&[0, 0, 1, 1]) - 0.5).abs() < 1e-6);
}
