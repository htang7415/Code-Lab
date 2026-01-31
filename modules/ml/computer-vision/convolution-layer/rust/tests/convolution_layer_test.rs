use ml_computer_vision_convolution_layer::conv2d;

#[test]
fn test_conv2d_shape() {
    let image = vec![vec![1.0, 2.0], vec![3.0, 4.0]];
    let kernel = vec![vec![1.0]];
    assert_eq!(conv2d(&image, &kernel), vec![vec![1.0, 2.0], vec![3.0, 4.0]]);
}
