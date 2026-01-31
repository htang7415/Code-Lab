fn matmul(a: &[Vec<f64>], b: &[Vec<f64>]) -> Vec<Vec<f64>> {
    let rows = a.len();
    let cols = b[0].len();
    let mut out = vec![vec![0.0; cols]; rows];
    for i in 0..rows {
        for j in 0..cols {
            let mut acc = 0.0;
            for k in 0..b.len() {
                acc += a[i][k] * b[k][j];
            }
            out[i][j] = acc;
        }
    }
    out
}

fn quantize(w: &[Vec<f64>], scale: f64) -> Vec<Vec<f64>> {
    w.iter()
        .map(|row| row.iter().map(|v| (v / scale).round() * scale).collect())
        .collect()
}

pub fn qlora_update(w: &[Vec<f64>], a: &[Vec<f64>], b: &[Vec<f64>], alpha: f64, scale: f64) -> Vec<Vec<f64>> {
    let w_q = quantize(w, scale);
    let r = b.len() as f64;
    let delta = matmul(a, b);
    let factor = alpha / r;
    let mut out = w_q;
    for i in 0..out.len() {
        for j in 0..out[0].len() {
            out[i][j] += factor * delta[i][j];
        }
    }
    out
}
