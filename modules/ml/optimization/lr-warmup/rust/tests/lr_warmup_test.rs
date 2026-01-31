use ml_optimization_lr_warmup::warmup_lr;

#[test]
fn test_warmup_lr() {
    assert!((warmup_lr(1.0, 5, 10) - 0.5).abs() < 1e-6);
}
