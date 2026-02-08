fn dot(a: &[f64], b: &[f64]) -> f64 {
    a.iter().zip(b.iter()).map(|(x, y)| x * y).sum()
}

fn sqdist(a: &[f64], b: &[f64]) -> f64 {
    a.iter()
        .zip(b.iter())
        .map(|(x, y)| {
            let d = x - y;
            d * d
        })
        .sum()
}

pub fn pegasos_kernel_svm(
    data: &[Vec<f64>],
    labels: &[f64],
    kernel: &str,
    lambda_val: f64,
    iterations: usize,
    sigma: f64,
) -> (Vec<f64>, f64) {
    let n = data.len();
    assert_eq!(
        labels.len(),
        n,
        "labels must be shape (n_samples,), got {}",
        labels.len()
    );
    if n == 0 {
        return (Vec::new(), 0.0);
    }

    let d = data[0].len();
    for row in data.iter().skip(1) {
        assert_eq!(row.len(), d, "all rows in data must have the same length");
    }

    assert!(
        kernel == "linear" || kernel == "rbf",
        "kernel must be 'linear' or 'rbf'"
    );
    assert!(lambda_val > 0.0, "lambda_val must be > 0");
    assert!(iterations > 0, "iterations must be > 0");
    if kernel == "rbf" {
        assert!(sigma > 0.0, "sigma must be > 0 for rbf kernel");
    }

    // Precompute kernel matrix K (n x n)
    let mut k_mat = vec![vec![0.0; n]; n];
    if kernel == "linear" {
        for i in 0..n {
            for j in 0..n {
                k_mat[i][j] = dot(&data[i], &data[j]);
            }
        }
    } else {
        let denom = 2.0 * sigma * sigma;
        for i in 0..n {
            for j in 0..n {
                let dist2 = sqdist(&data[i], &data[j]).max(0.0);
                k_mat[i][j] = (-dist2 / denom).exp();
            }
        }
    }

    let mut alpha = vec![0.0; n];
    let mut b = 0.0;

    for t in 1..=iterations {
        let eta = 1.0 / (lambda_val * t as f64);

        // Deterministic: fixed order, full pass over all samples
        for i in 0..n {
            // f(x_i) = sum_j alpha_j * y_j * K(x_j, x_i) + b
            let mut f_i = b;
            for j in 0..n {
                f_i += alpha[j] * labels[j] * k_mat[j][i];
            }

            if labels[i] * f_i < 1.0 {
                alpha[i] = alpha[i] + eta * (labels[i] - lambda_val * alpha[i]);
                b += eta * labels[i];
            }
        }
    }

    (alpha, b)
}
