def test_min_sum_square_diff_examples(solution):
    # Example 1: no modifications allowed.
    assert solution.minSumSquareDiff([1, 2, 3, 4], [2, 10, 20, 19], 0, 0) == 579

    # Example 2: one operation on each array.
    assert solution.minSumSquareDiff([1, 4, 10, 12], [5, 8, 6, 9], 1, 1) == 43


def test_min_sum_square_diff_all_equal(solution):
    # Identical arrays need no operations and have zero squared difference.
    assert solution.minSumSquareDiff([1, 1, 1], [1, 1, 1], 0, 0) == 0
