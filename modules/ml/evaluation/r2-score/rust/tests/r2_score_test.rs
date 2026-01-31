use ml_evaluation_r2_score::r2_score;

#[test]
fn test_r2_score() {
    assert!((r2_score(&[1.0, 2.0], &[1.0, 2.0]) - 1.0).abs() < 1e-6);
}
