pub fn pca_first_component_2d(points: &[Vec<f64>]) -> Vec<f64> {
    let n = points.len() as f64;
    let mean_x: f64 = points.iter().map(|p| p[0]).sum::<f64>() / n;
    let mean_y: f64 = points.iter().map(|p| p[1]).sum::<f64>() / n;
    let cov_xx: f64 = points.iter().map(|p| (p[0] - mean_x).powi(2)).sum::<f64>() / n;
    let cov_yy: f64 = points.iter().map(|p| (p[1] - mean_y).powi(2)).sum::<f64>() / n;
    let cov_xy: f64 = points.iter().map(|p| (p[0] - mean_x) * (p[1] - mean_y)).sum::<f64>() / n;
    let trace = cov_xx + cov_yy;
    let det = cov_xx * cov_yy - cov_xy * cov_xy;
    let eig1 = trace / 2.0 + ((trace / 2.0).powi(2) - det).max(0.0).sqrt();
    let (mut vx, mut vy) = if cov_xy == 0.0 {
        if cov_xx >= cov_yy { (1.0, 0.0) } else { (0.0, 1.0) }
    } else {
        (eig1 - cov_yy, cov_xy)
    };
    let norm = (vx * vx + vy * vy).sqrt();
    vx /= norm;
    vy /= norm;
    vec![vx, vy]
}
