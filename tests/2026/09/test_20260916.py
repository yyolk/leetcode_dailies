def test_number_of_sets_examples(solution):
    # Example 1
    assert solution.numberOfSets(4, 2) == 5

    # Example 2
    assert solution.numberOfSets(3, 1) == 3

    # Example 3
    assert solution.numberOfSets(30, 7) == 796297179


def test_number_of_sets_minimum_n(solution):
    # Only one segment is possible on two points: [0, 1].
    assert solution.numberOfSets(2, 1) == 1
