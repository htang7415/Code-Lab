use ml_generative_gan_mode_collapse::diversity_score;

#[test]
fn test_diversity_score() {
    assert!((diversity_score(&[1, 1, 1]) - 1.0 / 3.0).abs() < 1e-6);
}
