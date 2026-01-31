from stratified_split import stratified_split


def test_stratified_split():
    labels = [0, 0, 1, 1]
    train, test = stratified_split(labels, 0.5)
    assert len(train) == 2
    assert len(test) == 2
