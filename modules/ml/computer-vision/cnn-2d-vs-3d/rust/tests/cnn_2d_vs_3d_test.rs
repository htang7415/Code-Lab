use ml_computer_vision_cnn_2d_vs_3d::output_depth;

#[test]
fn test_output_depth() {
    assert_eq!(output_depth(5, 3), 3);
}
