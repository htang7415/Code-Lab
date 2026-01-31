use ml_computer_vision_bilinear_resizing::bilinear_sample;

#[test]
fn test_bilinear_sample() {
    assert!((bilinear_sample(0.0, 1.0, 1.0, 0.0, 0.5, 0.5) - 0.5).abs() < 1e-6);
}
