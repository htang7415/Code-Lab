use ml_models_knn::knn_predict;

#[test]
fn test_knn_predict() {
    let pred = knn_predict(&[0.1, 0.2, 0.3], &[1, 1, 0], 2);
    assert_eq!(pred, 1);
}
