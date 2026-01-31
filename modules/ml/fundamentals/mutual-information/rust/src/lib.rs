pub fn mutual_information(joint: &[Vec<f64>]) -> f64 {
    let px: Vec<f64> = joint.iter().map(|row| row.iter().sum()).collect();
    let mut py = vec![0.0; joint[0].len()];
    for i in 0..joint.len() {
        for j in 0..joint[0].len() {
            py[j] += joint[i][j];
        }
    }
    let mut mi = 0.0;
    for i in 0..joint.len() {
        for j in 0..joint[0].len() {
            let pxy = joint[i][j];
            if pxy > 0.0 && px[i] > 0.0 && py[j] > 0.0 {
                mi += pxy * (pxy / (px[i] * py[j])).ln();
            }
        }
    }
    mi
}
