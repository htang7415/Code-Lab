pub fn next_distribution(p: &[f64], t: &[Vec<f64>]) -> Vec<f64> {
    let mut out = vec![0.0; t[0].len()];
    for i in 0..t[0].len() {
        let mut sum = 0.0;
        for j in 0..p.len() {
            sum += p[j] * t[j][i];
        }
        out[i] = sum;
    }
    out
}
