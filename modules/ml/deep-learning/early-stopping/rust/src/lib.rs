pub fn should_stop(losses: &[f64], patience: usize) -> bool {
    let mut best = f64::INFINITY;
    let mut bad = 0;
    for &loss in losses {
        if loss < best {
            best = loss;
            bad = 0;
        } else {
            bad += 1;
            if bad >= patience {
                return true;
            }
        }
    }
    false
}
