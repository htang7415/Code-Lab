use ml_evaluation_f1_score::f1_score;

#[test]
fn test_f1_score() {
    assert!((f1_score(0.5, 0.5) - 0.5).abs() < 1e-6);
}
