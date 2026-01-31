pub fn mcc(tp: i32, tn: i32, fp: i32, fn_: i32) -> f64 {
    let denom = ((tp + fp) as f64 * (tp + fn_) as f64 * (tn + fp) as f64 * (tn + fn_) as f64).sqrt();
    if denom == 0.0 { 0.0 } else { (tp * tn - fp * fn_) as f64 / denom }
}
