pub fn warmup_lr(lr: f64, t: i32, warmup_steps: i32) -> f64 {
    let factor = (t as f64 / warmup_steps as f64).min(1.0);
    lr * factor
}
