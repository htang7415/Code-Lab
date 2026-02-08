use ml_models_svm_pegasos::pegasos_kernel_svm;

#[test]
fn test_pegasos_kernel_svm_linear_one_iteration() {
    let data = vec![vec![1.0, 0.0], vec![-1.0, 0.0]];
    let labels = vec![1.0, -1.0];
    let (alphas, bias) = pegasos_kernel_svm(&data, &labels, "linear", 1.0, 1, 1.0);
    assert_eq!(alphas, vec![1.0, -1.0]);
    assert_eq!(bias, 0.0);
}

#[test]
fn test_pegasos_kernel_svm_rbf_one_iteration() {
    let data = vec![vec![1.0, 0.0], vec![-1.0, 0.0]];
    let labels = vec![1.0, -1.0];
    let (alphas, bias) = pegasos_kernel_svm(&data, &labels, "rbf", 1.0, 1, 1.0);
    assert_eq!(alphas, vec![1.0, -1.0]);
    assert_eq!(bias, 0.0);
}
