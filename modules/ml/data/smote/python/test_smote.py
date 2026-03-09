from smote import smote_samples


def test_smote_samples_interpolate_between_neighbors():
    points = [[0.0, 0.0], [2.0, 2.0], [4.0, 4.0]]
    assert smote_samples(points, [(0, 1), (1, 2)], [0.25, 0.5]) == [
        [0.5, 0.5],
        [3.0, 3.0],
    ]


def test_smote_samples_zero_gap_repeats_base_point():
    assert smote_samples([[1.0, 3.0], [5.0, 7.0]], [(0, 1)], [0.0]) == [[1.0, 3.0]]
