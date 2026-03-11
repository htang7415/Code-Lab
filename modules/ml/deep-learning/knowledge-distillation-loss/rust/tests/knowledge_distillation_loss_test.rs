use ml_deep_learning_knowledge_distillation_loss::distill_loss;

#[test]
fn test_distill_loss_is_zero_for_matching_logits() {
    let loss = distill_loss(&[2.0, 0.0], &[2.0, 0.0], 1.0);
    assert!(loss < 1e-6);
}

#[test]
fn test_distill_loss_matches_teacher_to_student_kl() {
    let student = [2.0, 1.0, 0.0];
    let teacher = [0.0, 2.0, 1.0];

    let student_exps = [2.0_f64.exp(), 1.0_f64.exp(), 0.0_f64.exp()];
    let student_total: f64 = student_exps.iter().sum();
    let student_probs: Vec<f64> = student_exps.iter().map(|value| value / student_total).collect();

    let teacher_exps = [0.0_f64.exp(), 2.0_f64.exp(), 1.0_f64.exp()];
    let teacher_total: f64 = teacher_exps.iter().sum();
    let teacher_probs: Vec<f64> = teacher_exps.iter().map(|value| value / teacher_total).collect();

    let expected: f64 = teacher_probs
        .iter()
        .zip(student_probs.iter())
        .map(|(p_t, p_s)| p_t * (p_t / p_s).ln())
        .sum();

    assert!((distill_loss(&student, &teacher, 1.0) - expected).abs() < 1e-12);
}
