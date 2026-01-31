use ml_models_svm_pegasos::pegasos_step;

#[test]
fn test_pegasos_step() {
    let w = pegasos_step(&[0.0, 0.0], &[1.0, 0.0], 1, 0.1, 0.1);
    assert!(w[0] > 0.0);
}
