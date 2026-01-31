use ml_computer_vision_data_augmentation::horizontal_flip;

#[test]
fn test_horizontal_flip() {
    assert_eq!(horizontal_flip(&[vec![1, 2]]), vec![vec![2, 1]]);
}
