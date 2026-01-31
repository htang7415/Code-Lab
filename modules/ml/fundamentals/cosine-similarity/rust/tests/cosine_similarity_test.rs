use ml_fundamentals_cosine_similarity::cosine_similarity;

#[test]
fn test_cosine_similarity() {
    assert!((cosine_similarity(&[1.0, 0.0], &[1.0, 0.0]) - 1.0).abs() < 1e-6);
}
