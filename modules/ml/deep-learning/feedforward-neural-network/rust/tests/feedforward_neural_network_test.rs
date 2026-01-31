use ml_deep_learning_feedforward_neural_network::feedforward;

#[test]
fn test_feedforward_shape() {
    let x = vec![1.0, -1.0];
    let w1 = vec![vec![1.0, 0.0], vec![0.0, 1.0]];
    let b1 = vec![0.0, 0.0];
    let out = feedforward(&x, &[w1], &[b1]);
    assert_eq!(out.len(), 2);
}
