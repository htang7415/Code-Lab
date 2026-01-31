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

fn relu(row: &[f64]) -> Vec<f64> {
    row.iter().map(|x| x.max(0.0)).collect()
}

fn self_attention(x: &[Vec<f64>]) -> Vec<Vec<f64>> {
    let dk = x[0].len() as f64;
    let scores = matmul(x, &transpose(x));
    let scaled: Vec<Vec<f64>> = scores
        .iter()
        .map(|row| row.iter().map(|x| x / dk.sqrt()).collect())
        .collect();
    let weights: Vec<Vec<f64>> = scaled.iter().map(|row| softmax(row)).collect();
    matmul(&weights, x)
}

pub fn transformer_block(x: &[Vec<f64>], w1: &[Vec<f64>], w2: &[Vec<f64>]) -> Vec<Vec<f64>> {
    let attn = self_attention(x);
    let mut res1 = x.to_vec();
    for i in 0..res1.len() {
        for j in 0..res1[0].len() {
            res1[i][j] += attn[i][j];
        }
    }
    let ffn_hidden = matmul(&res1, w1);
    let ffn_hidden: Vec<Vec<f64>> = ffn_hidden.iter().map(|row| relu(row)).collect();
    let ffn = matmul(&ffn_hidden, w2);
    let mut res2 = res1.clone();
    for i in 0..res2.len() {
        for j in 0..res2[0].len() {
            res2[i][j] += ffn[i][j];
        }
    }
    res2
}
