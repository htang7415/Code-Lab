pub type Matrix = Vec<Vec<f64>>;

fn dot(a: &[f64], b: &[f64]) -> f64 {
    a.iter().zip(b.iter()).map(|(x, y)| x * y).sum()
}

fn norm(v: &[f64]) -> f64 {
    dot(v, v).sqrt()
}

pub fn gram_schmidt_rows(mat: &Matrix, eps: f64) -> Matrix {
    let mut out: Matrix = Vec::new();
    for row in mat.iter() {
        let mut v = row.clone();
        for u in out.iter() {
            let proj = dot(&v, u);
            for (vi, ui) in v.iter_mut().zip(u.iter()) {
                *vi -= proj * ui;
            }
        }
        let n = norm(&v);
        if n < eps {
            out.push(vec![0.0; v.len()]);
        } else {
            out.push(v.iter().map(|vi| vi / n).collect());
        }
    }
    out
}

pub fn muon_step(
    weights: &Matrix,
    grad: &Matrix,
    velocity: Option<&Matrix>,
    lr: f64,
    momentum: f64,
) -> (Matrix, Matrix) {
    let mut vel = match velocity {
        Some(v) => v.clone(),
        None => grad.iter().map(|row| vec![0.0; row.len()]).collect(),
    };
    for (v_row, g_row) in vel.iter_mut().zip(grad.iter()) {
        for (v, g) in v_row.iter_mut().zip(g_row.iter()) {
            *v = momentum * *v + *g;
        }
    }
    let ortho = gram_schmidt_rows(&vel, 1e-12);
    let mut new_weights = weights.clone();
    for (w_row, u_row) in new_weights.iter_mut().zip(ortho.iter()) {
        for (w, u) in w_row.iter_mut().zip(u_row.iter()) {
            *w -= lr * u;
        }
    }
    (new_weights, vel)
}
