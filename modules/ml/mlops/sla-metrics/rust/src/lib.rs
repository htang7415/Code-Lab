pub fn violation_rate(violations: i32, total: i32) -> f64 {
    if total > 0 { violations as f64 / total as f64 } else { 0.0 }
}
