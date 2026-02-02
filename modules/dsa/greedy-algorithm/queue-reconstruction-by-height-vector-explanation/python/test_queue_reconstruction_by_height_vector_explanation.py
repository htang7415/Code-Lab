from queue_reconstruction_by_height_vector_explanation import Solution


def test_queue_reconstruction_vector_explanation():
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    assert Solution().reconstructQueue(people) == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
