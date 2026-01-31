pub fn sinusoidal_position(pos: usize, d_model: usize) -> Vec<f64> {
    let mut values = Vec::with_capacity(d_model);
    for i in 0..d_model {
        let angle = (pos as f64) / 10000f64.powf(2.0 * ((i / 2) as f64) / d_model as f64);
        if i % 2 == 0 {
            values.push(angle.sin());
        } else {
            values.push(angle.cos());
        }
    }
    values
}
