use ml_fundamentals_markov_chains::next_distribution;

#[test]
fn test_next_distribution() {
    let p = vec![1.0, 0.0];
    let t = vec![vec![0.0, 1.0], vec![1.0, 0.0]];
    assert_eq!(next_distribution(&p, &t), vec![0.0, 1.0]);
}
