use ml_models_k_means::assign;

#[test]
fn test_assign() {
    let points = vec![vec![0.0], vec![10.0]];
    let centroids = vec![vec![0.0], vec![5.0]];
    assert_eq!(assign(&points, &centroids), vec![0, 1]);
}
