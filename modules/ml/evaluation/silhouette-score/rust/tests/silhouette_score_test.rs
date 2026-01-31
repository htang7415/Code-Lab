use ml_evaluation_silhouette_score::silhouette;

#[test]
fn test_silhouette() {
    assert!((silhouette(0.2, 0.6) - 2.0/3.0).abs() < 1e-6);
}
