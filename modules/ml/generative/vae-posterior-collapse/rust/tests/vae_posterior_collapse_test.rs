use ml_generative_vae_posterior_collapse::kl_is_low;

#[test]
fn test_kl_is_low() {
    assert!(kl_is_low(0.05, 0.1));
}
