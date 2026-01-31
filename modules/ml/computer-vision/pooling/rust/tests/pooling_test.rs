use ml_computer_vision_pooling::{max_pool, avg_pool};

#[test]
fn test_pooling() {
    assert_eq!(max_pool(&[1.0, 3.0, 2.0]), 3.0);
    assert_eq!(avg_pool(&[1.0, 3.0]), 2.0);
}
