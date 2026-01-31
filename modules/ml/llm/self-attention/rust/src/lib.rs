fn softmax(row: &[f64]) -> Vec<f64> {
    let m = row.iter().copied().fold(f64::NEG_INFINITY, f64::max);
    let exps: Vec<f64> = row.iter().map(|x| (x - m).exp()).collect();
    let sum: f64 = exps.iter().sum();
    exps.iter().map(|e| e / sum).collect()
}

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

fn transpose(a: &[Vec<f64>]) -> Vec<Vec<f64>> {
    let rows = a.len();
    let cols = a[0].len();
    let mut out = vec![vec![0.0; rows]; cols];
    for i in 0..rows {
        for j in 0..cols {
            out[j][i] = a[i][j];
        }
    }
    out
}

pub fn self_attention(q: &[Vec<f64>], k: &[Vec<f64>], v: &[Vec<f64>]) -> Vec<Vec<f64>> {
    let dk = k[0].len() as f64;
    let scores = matmul(q, &transpose(k));
    let scaled: Vec<Vec<f64>> = scores
        .iter()
        .map(|row| row.iter().map(|x| x / dk.sqrt()).collect())
        .collect();
    let weights: Vec<Vec<f64>> = scaled.iter().map(|row| softmax(row)).collect();
    matmul(&weights, v)
}
