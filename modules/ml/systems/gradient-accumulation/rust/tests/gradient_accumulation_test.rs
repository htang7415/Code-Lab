use ml_systems_gradient_accumulation::accumulate;

#[test]
fn test_accumulate() {
    assert_eq!(accumulate(&[vec![1.0, 2.0], vec![3.0, 4.0]]), vec![4.0, 6.0]);
}
