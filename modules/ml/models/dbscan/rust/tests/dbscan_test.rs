use ml_models_dbscan::neighbors;

#[test]
fn test_neighbors() {
    let points = vec![vec![0.0], vec![0.1], vec![2.0]];
    assert_eq!(neighbors(&points, 0, 0.2), vec![0, 1]);
}
