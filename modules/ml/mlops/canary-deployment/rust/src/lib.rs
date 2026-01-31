pub fn split_traffic(total: i32, canary_pct: f64) -> (i32, i32) {
    let canary = (total as f64 * canary_pct) as i32;
    (canary, total - canary)
}
