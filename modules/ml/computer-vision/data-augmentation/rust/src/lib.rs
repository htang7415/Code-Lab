pub fn horizontal_flip(image: &[Vec<i32>]) -> Vec<Vec<i32>> {
    let mut out = Vec::new();
    for row in image {
        let mut r = row.clone();
        r.reverse();
        out.push(r);
    }
    out
}
