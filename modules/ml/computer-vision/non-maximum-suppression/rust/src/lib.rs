pub fn iou(a: (f64, f64, f64, f64), b: (f64, f64, f64, f64)) -> f64 {
    let (ax1, ay1, ax2, ay2) = a;
    let (bx1, by1, bx2, by2) = b;
    let inter_x1 = ax1.max(bx1);
    let inter_y1 = ay1.max(by1);
    let inter_x2 = ax2.min(bx2);
    let inter_y2 = ay2.min(by2);
    if inter_x2 <= inter_x1 || inter_y2 <= inter_y1 {
        return 0.0;
    }
    let inter = (inter_x2 - inter_x1) * (inter_y2 - inter_y1);
    let area_a = (ax2 - ax1) * (ay2 - ay1);
    let area_b = (bx2 - bx1) * (by2 - by1);
    inter / (area_a + area_b - inter)
}
