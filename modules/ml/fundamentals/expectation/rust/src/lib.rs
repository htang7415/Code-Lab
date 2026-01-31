pub fn expectation(values: &[f64], probs: &[f64]) -> f64 {
    values.iter().zip(probs.iter()).map(|(v, p)| v * p).sum()
}
