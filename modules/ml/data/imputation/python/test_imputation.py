from imputation import mean_impute


def test_mean_impute_columnwise():
    table = [
        [1.0, None],
        [3.0, 6.0],
        [None, 9.0],
    ]
    assert mean_impute(table) == [
        [1.0, 7.5],
        [3.0, 6.0],
        [2.0, 9.0],
    ]


def test_mean_impute_all_missing_column_defaults_to_zero():
    table = [
        [None],
        [None],
    ]
    assert mean_impute(table) == [[0.0], [0.0]]
