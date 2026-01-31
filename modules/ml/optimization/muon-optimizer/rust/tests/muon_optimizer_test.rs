use ml_optimization_muon_optimizer::{gram_schmidt_rows, muon_step, Matrix};

#[test]
fn test_gram_schmidt_rows_orthogonal() {
    let mat: Matrix = vec![vec![1.0, 2.0], vec![3.0, 4.0]];
    let q = gram_schmidt_rows(&mat, 1e-12);
    let dot = q[0][0] * q[1][0] + q[0][1] * q[1][1];
    assert!(dot.abs() < 1e-6);
}

#[test]
fn test_muon_step_updates_weights() {
    let weights: Matrix = vec![vec![1.0, 0.0], vec![0.0, 1.0]];
    let grad: Matrix = vec![vec![1.0, 0.0], vec![0.0, 1.0]];
    let (new_weights, velocity) = muon_step(&weights, &grad, None, 0.1, 0.0);
    assert_eq!(velocity, grad);
    assert!(new_weights[0][0] != weights[0][0]);
}
