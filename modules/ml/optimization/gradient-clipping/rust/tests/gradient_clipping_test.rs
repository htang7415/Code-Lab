use ml_optimization_gradient_clipping::clip_norm;

#[test]
fn test_clip_norm() {
    let grad = clip_norm(&[3.0, 4.0], 5.0);
    assert_eq!(grad, vec![3.0, 4.0]);
    let grad2 = clip_norm(&[3.0, 4.0], 2.5);
    let norm = (grad2.iter().map(|g| g * g).sum::<f64>()).sqrt();
    assert!(norm <= 2.5 + 1e-6);
}
