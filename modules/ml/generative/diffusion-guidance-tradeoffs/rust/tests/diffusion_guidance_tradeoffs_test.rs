use ml_generative_diffusion_guidance_tradeoffs::guided_step;

#[test]
fn test_guided_step() {
    assert!((guided_step(0.0, 1.0, 0.5) - 0.5).abs() < 1e-6);
}
