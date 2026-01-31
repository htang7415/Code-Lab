use ml_fundamentals_svd::singular_values_2x2;

#[test]
fn test_singular_values() {
    let vals = singular_values_2x2([[1.0, 0.0], [0.0, 2.0]]);
    let mut sorted = vals.to_vec();
    sorted.sort_by(|a, b| a.partial_cmp(b).unwrap());
    assert_eq!(sorted, vec![1.0, 2.0]);
}
