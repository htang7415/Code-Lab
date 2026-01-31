from dataset_batch_epoch import num_batches


def test_num_batches():
    assert num_batches(10, 4) == 3
