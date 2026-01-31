pub fn mean_shift(old: &[f64], new: &[f64]) -> f64 {
    let mean_old: f64 = old.iter().sum::<f64>() / old.len() as f64;
    let mean_new: f64 = new.iter().sum::<f64>() / new.len() as f64;
    (mean_new - mean_old).abs()
}
