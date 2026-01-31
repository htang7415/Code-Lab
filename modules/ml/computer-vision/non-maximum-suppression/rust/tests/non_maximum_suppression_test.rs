use ml_computer_vision_non_maximum_suppression::iou;

#[test]
fn test_iou() {
    assert!((iou((0.0, 0.0, 1.0, 1.0), (0.0, 0.0, 1.0, 1.0)) - 1.0).abs() < 1e-6);
}
