pub fn conv2d(image: &[Vec<f64>], kernel: &[Vec<f64>]) -> Vec<Vec<f64>> {
    let h = image.len();
    let w = image[0].len();
    let kh = kernel.len();
    let kw = kernel[0].len();
    let mut out = Vec::new();
    for i in 0..=h - kh {
        let mut row = Vec::new();
        for j in 0..=w - kw {
            let mut val = 0.0;
            for u in 0..kh {
                for v in 0..kw {
                    val += image[i + u][j + v] * kernel[u][v];
                }
            }
            row.push(val);
        }
        out.push(row);
    }
    out
}
