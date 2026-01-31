use ml_computer_vision_cnn_basics::conv1d;

#[test]
fn test_conv1d() {
    assert_eq!(conv1d(&[1.0, 2.0, 3.0], &[1.0, 0.0]), vec![1.0, 2.0]);
}
