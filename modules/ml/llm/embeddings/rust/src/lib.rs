pub fn embed(tokens: &[usize], embeddings: &[Vec<f64>]) -> Vec<Vec<f64>> {
    tokens.iter().map(|&i| embeddings[i].clone()).collect()
}
