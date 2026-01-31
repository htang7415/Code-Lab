pub fn neuron(x: &[f64], w: &[f64], b: f64) -> f64 {
    let mut z = b;
    for (wi, xi) in w.iter().zip(x.iter()) {
        z += wi * xi;
    }
    1.0 / (1.0 + (-z).exp())
}
