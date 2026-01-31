use ml_deep_learning_activations_sigmoid_tanh::{activations, dynamic_tanh};

#[test]
fn test_activations_range() {
    let (sigmoid, tanh, _, _, _) = activations(2.0);
    assert!(sigmoid >= 0.0 && sigmoid <= 1.0);
    assert!(tanh >= -1.0 && tanh <= 1.0);
}

#[test]
fn test_dynamic_tanh_parameters() {
    let out = dynamic_tanh(0.0, 2.0, 3.0, 0.5);
    assert!((out - 0.5).abs() < 1e-12);
}
