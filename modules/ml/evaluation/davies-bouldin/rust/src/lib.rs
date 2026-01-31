pub fn davies_bouldin(si: f64, sj: f64, dij: f64) -> f64 {
    if dij > 0.0 { (si + sj) / dij } else { 0.0 }
}
