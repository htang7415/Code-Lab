use ml_computer_vision_contrast_brightness::adjust;

#[test]
fn test_adjust() {
    assert_eq!(adjust(10.0, 1.0, 5.0), 15.0);
}
