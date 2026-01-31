use ml_generative_diffusion_models::add_noise;

#[test]
fn test_add_noise() {
    assert!((add_noise(1.0, 0.0, 1.0) - 1.0).abs() < 1e-6);
}
