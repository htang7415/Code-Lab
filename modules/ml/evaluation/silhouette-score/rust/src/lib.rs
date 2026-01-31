pub fn silhouette(a: f64, b: f64) -> f64 {
    let m = a.max(b);
    if m == 0.0 { 0.0 } else { (b - a) / m }
}
