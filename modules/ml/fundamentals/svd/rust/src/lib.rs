pub fn svd_2x2(a: [[f64; 2]; 2]) -> ([[f64; 2]; 2], [f64; 2], [[f64; 2]; 2]) {
    let a00 = a[0][0];
    let a01 = a[0][1];
    let a10 = a[1][0];
    let a11 = a[1][1];

    let b00 = a00 * a00 + a10 * a10;
    let b01 = a00 * a01 + a10 * a11;
    let b11 = a01 * a01 + a11 * a11;

    let eps = 1e-12_f64;

    let (c, s) = if b01.abs() <= eps {
        (1.0, 0.0)
    } else {
        let tau = (b11 - b00) / (2.0 * b01);
        let t = if tau == 0.0 {
            1.0
        } else {
            tau.signum() / (tau.abs() + (1.0 + tau * tau).sqrt())
        };
        let c = 1.0 / (1.0 + t * t).sqrt();
        let s = t * c;
        (c, s)
    };

    let mut v00 = c;
    let mut v01 = -s;
    let mut v10 = s;
    let mut v11 = c;

    let cs = c * s;
    let c2 = c * c;
    let s2 = s * s;
    let mut lam1 = c2 * b00 - 2.0 * cs * b01 + s2 * b11;
    let mut lam2 = s2 * b00 + 2.0 * cs * b01 + c2 * b11;

    if lam1 < 0.0 {
        lam1 = 0.0;
    }
    if lam2 < 0.0 {
        lam2 = 0.0;
    }

    let mut s0 = lam1.sqrt();
    let mut s1 = lam2.sqrt();

    if s1 > s0 {
        std::mem::swap(&mut s0, &mut s1);
        std::mem::swap(&mut v00, &mut v01);
        std::mem::swap(&mut v10, &mut v11);
    }

    let vt = [[v00, v10], [v01, v11]];

    if s0 <= eps {
        return ([[1.0, 0.0], [0.0, 1.0]], [0.0, 0.0], [[1.0, 0.0], [0.0, 1.0]]);
    }

    let av00 = a00 * v00 + a01 * v10;
    let av10 = a10 * v00 + a11 * v10;
    let av01 = a00 * v01 + a01 * v11;
    let av11 = a10 * v01 + a11 * v11;

    let u00 = av00 / s0;
    let u10 = av10 / s0;

    let (u01, u11) = if s1 > eps {
        (av01 / s1, av11 / s1)
    } else {
        (-u10, u00)
    };

    let u = [[u00, u01], [u10, u11]];
    (u, [s0, s1], vt)
}

pub fn singular_values_2x2(a: [[f64; 2]; 2]) -> [f64; 2] {
    let (_, svals, _) = svd_2x2(a);
    svals
}
