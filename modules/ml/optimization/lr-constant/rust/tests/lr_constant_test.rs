use ml_optimization_lr_constant::constant_lr;

#[test]
fn test_constant_lr() {
    assert_eq!(constant_lr(0.1), 0.1);
}
