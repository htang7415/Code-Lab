use ml_fundamentals_mutual_information::mutual_information;

#[test]
fn test_mutual_information() {
    let joint = vec![vec![0.25, 0.25], vec![0.25, 0.25]];
    assert!((mutual_information(&joint) - 0.0).abs() < 1e-6);
}
