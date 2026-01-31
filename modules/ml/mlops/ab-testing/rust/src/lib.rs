pub fn conversion_rate(conversions: i32, trials: i32) -> f64 {
    if trials > 0 { conversions as f64 / trials as f64 } else { 0.0 }
}
