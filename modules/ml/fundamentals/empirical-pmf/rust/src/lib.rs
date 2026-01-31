use std::collections::HashMap;

pub fn empirical_pmf(samples: &[i32]) -> HashMap<i32, f64> {
    let mut counts: HashMap<i32, usize> = HashMap::new();
    for s in samples {
        *counts.entry(*s).or_insert(0) += 1;
    }
    let n = samples.len() as f64;
    let mut pmf = HashMap::new();
    for (k, v) in counts {
        pmf.insert(k, v as f64 / n);
    }
    pmf
}
