use ml_reinforcement_learning_bandit_epsilon_greedy::EpsilonGreedyBandit;

#[test]
fn test_update_and_greedy_selection() {
    let mut bandit = EpsilonGreedyBandit::new(2, 0.0, 123);
    bandit.update(1, 1.0);
    assert_eq!(bandit.counts()[1], 1);
    let arm = bandit.select_arm();
    assert_eq!(arm, 1);
}
