use ml_deep_learning_neuron_weights_bias_activation::neuron;

#[test]
fn test_neuron_output_range() {
    let out = neuron(&[1.0, 1.0], &[1.0, 1.0], 0.0);
    assert!(out > 0.0 && out < 1.0);
}
