from gradient_boosting import gradient_boosting_step


def test_gradient_boosting_step_updates_predictions_and_residuals():
    updated, residuals = gradient_boosting_step(
        targets=[3.0, 5.0],
        predictions=[1.0, 2.0],
        weak_learner_output=[2.0, 3.0],
        learning_rate=0.5,
    )
    assert updated == [2.0, 3.5]
    assert residuals == [1.0, 1.5]
