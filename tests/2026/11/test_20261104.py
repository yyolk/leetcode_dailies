def test_min_operations_examples(solution):
    # Official Example 1
    assert solution.minOperations(
        [5, -2, 1, 3, 7, 3, 6, 4, -1], 3, 2
    ) == 8

    # Official Example 2
    assert solution.minOperations(
        [9, -2, -2, -2, 1, 5], 2, 2
    ) == 3
