pub fn pegasos_step(w: &[f64], x: &[f64], y: i32, lr: f64, lam: f64) -> Vec<f64> {
    let dot: f64 = w.iter().zip(x.iter()).map(|(wi, xi)| wi * xi).sum();
    let scale = 1.0 - lr * lam;
    let mut out: Vec<f64> = w.iter().map(|wi| wi * scale).collect();
    if (y as f64) * dot < 1.0 {
        for i in 0..out.len() {
            out[i] += lr * (y as f64) * x[i];
        }
    }
    out
}
