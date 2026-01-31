pub fn discounted_return(rewards: &[f64], gamma: f64) -> f64 {
    let mut total = 0.0;
    for (i, r) in rewards.iter().enumerate() {
        total += gamma.powi(i as i32) * r;
    }
    total
}
