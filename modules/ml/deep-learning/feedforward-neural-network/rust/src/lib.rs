pub fn feedforward(
    x: &[f64],
    weights: &[Vec<Vec<f64>>],
    biases: &[Vec<f64>],
) -> Vec<f64> {
    let mut h: Vec<f64> = x.to_vec();
    for (w, b) in weights.iter().zip(biases.iter()) {
        let mut next = vec![0.0; w.len()];
        for i in 0..w.len() {
            let mut acc = 0.0;
            for j in 0..h.len() {
                acc += w[i][j] * h[j];
            }
            next[i] = (acc + b[i]).max(0.0);
        }
        h = next;
    }
    h
}
