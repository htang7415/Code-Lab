struct Lcg {
    state: u64,
}

impl Lcg {
    fn new(seed: u64) -> Self {
        Self { state: seed }
    }

    fn next_u32(&mut self) -> u32 {
        self.state = self
            .state
            .wrapping_mul(6364136223846793005)
            .wrapping_add(1);
        (self.state >> 32) as u32
    }

    fn next_f64(&mut self) -> f64 {
        let v = self.next_u32() as f64;
        v / u32::MAX as f64
    }

    fn gen_range(&mut self, upper: usize) -> usize {
        (self.next_u32() as usize) % upper
    }
}

pub struct EpsilonGreedyBandit {
    k: usize,
    epsilon: f64,
    q_values: Vec<f64>,
    counts: Vec<usize>,
    rng: Lcg,
}

impl EpsilonGreedyBandit {
    pub fn new(k: usize, epsilon: f64, seed: u64) -> Self {
        Self {
            k,
            epsilon,
            q_values: vec![0.0; k],
            counts: vec![0; k],
            rng: Lcg::new(seed),
        }
    }

    pub fn select_arm(&mut self) -> usize {
        if self.rng.next_f64() < self.epsilon {
            return self.rng.gen_range(self.k);
        }
        let max_q = self
            .q_values
            .iter()
            .cloned()
            .fold(f64::NEG_INFINITY, f64::max);
        let mut best: Vec<usize> = self
            .q_values
            .iter()
            .enumerate()
            .filter(|(_, q)| **q == max_q)
            .map(|(i, _)| i)
            .collect();
        if best.len() == 1 {
            return best[0];
        }
        let idx = self.rng.gen_range(best.len());
        best.swap_remove(idx)
    }

    pub fn update(&mut self, arm: usize, reward: f64) {
        self.counts[arm] += 1;
        let n = self.counts[arm] as f64;
        self.q_values[arm] += (reward - self.q_values[arm]) / n;
    }

    pub fn q_values(&self) -> &[f64] {
        &self.q_values
    }

    pub fn counts(&self) -> &[usize] {
        &self.counts
    }
}
