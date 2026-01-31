use ml_computer_vision_image_preprocessing::normalize_pixels;

#[test]
fn test_normalize_pixels() {
    assert_eq!(normalize_pixels(&[0, 255]), vec![0.0, 1.0]);
}
