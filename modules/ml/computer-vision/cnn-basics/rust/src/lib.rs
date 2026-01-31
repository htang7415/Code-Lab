pub fn conv1d(signal: &[f64], kernel: &[f64]) -> Vec<f64> {
    let k = kernel.len();
    let mut out = Vec::new();
    for i in 0..=signal.len() - k {
        let mut acc = 0.0;
        for j in 0..k {
            acc += signal[i + j] * kernel[j];
        }
        out.push(acc);
    }
    out
}
