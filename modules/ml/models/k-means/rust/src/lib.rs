pub fn assign(points: &[Vec<f64>], centroids: &[Vec<f64>]) -> Vec<usize> {
    let mut assignments = Vec::with_capacity(points.len());
    for p in points {
        let mut best = 0;
        let mut best_dist = f64::INFINITY;
        for (i, c) in centroids.iter().enumerate() {
            let dist: f64 = p.iter().zip(c.iter()).map(|(pi, ci)| (pi - ci).powi(2)).sum();
            if dist < best_dist {
                best_dist = dist;
                best = i;
            }
        }
        assignments.push(best);
    }
    assignments
}
