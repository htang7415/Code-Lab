use ml_fundamentals_vectors_matrices::matvec;

#[test]
fn test_matvec() {
    assert_eq!(matvec(&[vec![1.0, 0.0], vec![0.0, 1.0]], &[2.0, 3.0]), vec![2.0, 3.0]);
}
