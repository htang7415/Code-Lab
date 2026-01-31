use ml_computer_vision_sobel_edge_detection::sobel_center;

#[test]
fn test_sobel_center() {
    let patch = vec![vec![0.0, 0.0, 0.0], vec![0.0, 1.0, 0.0], vec![0.0, 0.0, 0.0]];
    assert_eq!(sobel_center(&patch), 0.0);
}
