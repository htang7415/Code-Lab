use ml_computer_vision_rgb_to_grayscale::rgb_to_gray;

#[test]
fn test_rgb_to_gray() {
    assert_eq!(rgb_to_gray(255, 255, 255).round(), 255.0);
}
