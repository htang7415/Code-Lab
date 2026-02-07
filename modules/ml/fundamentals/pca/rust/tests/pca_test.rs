use ml_models_pca::pca_first_component_2d;

#[test]
fn test_pca_first_component() {
    let points = vec![vec![-1.0, 0.0], vec![1.0, 0.0]];
    let vec = pca_first_component_2d(&points);
    assert!((vec[0].abs() - 1.0).abs() < 1e-6);
}
