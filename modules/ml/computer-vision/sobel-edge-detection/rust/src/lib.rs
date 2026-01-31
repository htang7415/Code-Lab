pub fn sobel_center(patch: &[Vec<f64>]) -> f64 {
    let gx = -1.0 * patch[0][0] + 1.0 * patch[0][2]
        -2.0 * patch[1][0] + 2.0 * patch[1][2]
        -1.0 * patch[2][0] + 1.0 * patch[2][2];
    let gy = -1.0 * patch[0][0] - 2.0 * patch[0][1] - 1.0 * patch[0][2]
        + 1.0 * patch[2][0] + 2.0 * patch[2][1] + 1.0 * patch[2][2];
    (gx * gx + gy * gy).sqrt()
}
