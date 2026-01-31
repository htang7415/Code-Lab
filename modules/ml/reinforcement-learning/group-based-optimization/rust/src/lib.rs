pub fn group_advantages(rewards: &[f64]) -> Vec<f64> {
    if rewards.is_empty() {
        return Vec::new();
    }
    let mean = rewards.iter().sum::<f64>() / rewards.len() as f64;
    let var = rewards
        .iter()
        .map(|r| (r - mean).powi(2))
        .sum::<f64>()
        / rewards.len() as f64;
    let std = var.sqrt();
    rewards
        .iter()
        .map(|r| (r - mean) / (std + 1e-8))
        .collect()
}

fn sequence_ratio(old_logps: &[f64], new_logps: &[f64]) -> f64 {
    let sum_delta: f64 = old_logps
        .iter()
        .zip(new_logps.iter())
        .map(|(o, n)| n - o)
        .sum();
    sum_delta.exp()
}

fn token_ratio_mean(old_logps: &[f64], new_logps: &[f64]) -> f64 {
    let ratios: f64 = old_logps
        .iter()
        .zip(new_logps.iter())
        .map(|(o, n)| (n - o).exp())
        .sum();
    ratios / old_logps.len() as f64
}

pub fn grpo_objective(old_logps: &[Vec<f64>], new_logps: &[Vec<f64>], rewards: &[f64]) -> f64 {
    let advantages = group_advantages(rewards);
    if advantages.is_empty() {
        return 0.0;
    }
    let mut total = 0.0;
    for ((old, new), adv) in old_logps.iter().zip(new_logps.iter()).zip(advantages.iter()) {
        total += token_ratio_mean(old, new) * adv;
    }
    total / advantages.len() as f64
}

pub fn gspo_objective(old_logps: &[Vec<f64>], new_logps: &[Vec<f64>], rewards: &[f64]) -> f64 {
    let advantages = group_advantages(rewards);
    if advantages.is_empty() {
        return 0.0;
    }
    let mut total = 0.0;
    for ((old, new), adv) in old_logps.iter().zip(new_logps.iter()).zip(advantages.iter()) {
        total += sequence_ratio(old, new) * adv;
    }
    total / advantages.len() as f64
}
