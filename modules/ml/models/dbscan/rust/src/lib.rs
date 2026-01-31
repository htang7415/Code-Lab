pub fn neighbors(points: &[Vec<f64>], idx: usize, eps: f64) -> Vec<usize> {
    let base = &points[idx];
    let mut out = Vec::new();
    for (i, p) in points.iter().enumerate() {
        let dist = base
            .iter()
            .zip(p.iter())
            .map(|(a, b)| (a - b).powi(2))
            .sum::<f64>()
            .sqrt();
        if dist <= eps {
            out.push(i);
        }
    }
    out
}
