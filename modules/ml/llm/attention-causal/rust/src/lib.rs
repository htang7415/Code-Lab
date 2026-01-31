pub fn causal_mask(seq_len: usize) -> Vec<Vec<f64>> {
    let mut mask = vec![vec![0.0; seq_len]; seq_len];
    for i in 0..seq_len {
        for j in (i + 1)..seq_len {
            mask[i][j] = f64::NEG_INFINITY;
        }
    }
    mask
}

fn softmax(row: &[f64]) -> Vec<f64> {
    let m = row
        .iter()
        .copied()
        .fold(f64::NEG_INFINITY, f64::max);
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

pub fn causal_self_attention(q: &[Vec<f64>], k: &[Vec<f64>], v: &[Vec<f64>]) -> Vec<Vec<f64>> {
    let dk = k[0].len() as f64;
    let scores = matmul(q, &transpose(k));
    let mask = causal_mask(scores.len());
    let mut masked = scores.clone();
    for i in 0..scores.len() {
        for j in 0..scores[0].len() {
            masked[i][j] = scores[i][j] / dk.sqrt() + mask[i][j];
        }
    }
    let weights: Vec<Vec<f64>> = masked.iter().map(|row| softmax(row)).collect();
    matmul(&weights, v)
}
