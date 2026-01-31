pub fn singular_values_2x2(a: [[f64; 2]; 2]) -> [f64; 2] {
    let at_a = [
        [a[0][0] * a[0][0] + a[1][0] * a[1][0], a[0][0] * a[0][1] + a[1][0] * a[1][1]],
        [a[0][0] * a[0][1] + a[1][0] * a[1][1], a[0][1] * a[0][1] + a[1][1] * a[1][1]],
    ];
    let trace = at_a[0][0] + at_a[1][1];
    let det = at_a[0][0] * at_a[1][1] - at_a[0][1] * at_a[1][0];
    let disc = ((trace / 2.0).powi(2) - det).max(0.0).sqrt();
    let eig1 = trace / 2.0 + disc;
    let eig2 = trace / 2.0 - disc;
    [eig1.sqrt(), eig2.sqrt()]
}
