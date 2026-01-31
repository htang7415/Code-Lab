use std::collections::HashMap;

pub fn transition_prob(
    transitions: &HashMap<(i32, i32), HashMap<i32, f64>>,
    s: i32,
    a: i32,
    s_next: i32,
) -> f64 {
    transitions
        .get(&(s, a))
        .and_then(|m| m.get(&s_next).copied())
        .unwrap_or(0.0)
}
