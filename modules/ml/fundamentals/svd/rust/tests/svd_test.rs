use ml_fundamentals_svd::{singular_values_2x2, svd_2x2};

fn matmul_2x2(a: [[f64; 2]; 2], b: [[f64; 2]; 2]) -> [[f64; 2]; 2] {
    [
        [
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ],
        [
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ],
    ]
}

fn diag_2x2(s: [f64; 2]) -> [[f64; 2]; 2] {
    [[s[0], 0.0], [0.0, s[1]]]
}

fn assert_mat_close(a: [[f64; 2]; 2], b: [[f64; 2]; 2], tol: f64) {
    for i in 0..2 {
        for j in 0..2 {
            assert!((a[i][j] - b[i][j]).abs() <= tol);
        }
    }
}

#[test]
fn test_singular_values() {
    let vals = singular_values_2x2([[1.0, 0.0], [0.0, 2.0]]);
    let mut sorted = vals.to_vec();
    sorted.sort_by(|a, b| a.partial_cmp(b).unwrap());
    assert_eq!(sorted, vec![1.0, 2.0]);
}

#[test]
fn test_svd_reconstruction() {
    let a = [[3.0, 1.0], [0.0, 2.0]];
    let (u, svals, vt) = svd_2x2(a);
    let us = matmul_2x2(u, diag_2x2(svals));
    let a_hat = matmul_2x2(us, vt);
    assert_mat_close(a_hat, a, 1e-8);
}
