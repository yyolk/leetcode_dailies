def test_min_operations_examples(solution):
    # Example 1: remove last two elements [2, 3]
    assert solution.minOperations([1, 1, 4, 2, 3], 5) == 2

    # Example 2: no prefix/suffix sums to 4
    assert solution.minOperations([5, 6, 7, 8, 9], 4) == -1

    # Example 3: remove first two and last three
    assert solution.minOperations([3, 2, 20, 1, 1, 3], 10) == 5


def test_min_operations_whole_array(solution):
    # Entire array sums to x: must remove every element
    assert solution.minOperations([1, 1], 2) == 2
