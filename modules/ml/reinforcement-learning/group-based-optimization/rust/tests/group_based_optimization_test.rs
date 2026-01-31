use ml_reinforcement_learning_group_based_optimization::{
    group_advantages, grpo_objective, gspo_objective,
};

#[test]
fn test_group_advantages_centered() {
    let rewards = vec![0.0, 1.0];
    let adv = group_advantages(&rewards);
    assert_eq!(adv.len(), 2);
    assert!((adv[0] + adv[1]).abs() < 1e-9);
}

#[test]
fn test_objectives_match_expected() {
    let rewards = vec![0.0, 1.0];
    let old_logps = vec![vec![-0.1, -0.1], vec![-0.2, -0.2]];
    let new_logps = vec![vec![-0.2, -0.2], vec![-0.2, -0.2]];

    let gspo = gspo_objective(&old_logps, &new_logps, &rewards);
    let grpo = grpo_objective(&old_logps, &new_logps, &rewards);

    let seq_ratio = ((-0.2_f64 + 0.1) + (-0.2 + 0.1)).exp();
    let token_ratio = (-0.1_f64).exp();
    let expected_gspo = (-seq_ratio + 1.0) / 2.0;
    let expected_grpo = (-token_ratio + 1.0) / 2.0;

    assert!((gspo - expected_gspo).abs() < 1e-6);
    assert!((grpo - expected_grpo).abs() < 1e-6);
}
