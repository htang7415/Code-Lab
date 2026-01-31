use ml_optimization_loss_scaling::scale_grad;

#[test]
fn test_scale_grad() {
    assert_eq!(scale_grad(0.5, 8.0), 4.0);
}
