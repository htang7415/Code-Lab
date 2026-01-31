use ml_evaluation_confusion_matrix::confusion_matrix;

#[test]
fn test_confusion_matrix() {
    assert_eq!(confusion_matrix(&[0, 1], &[0, 0]), [[1, 0], [1, 0]]);
}
