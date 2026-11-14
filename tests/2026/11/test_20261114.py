def test_minimum_sum_subarray_examples(solution):
    # Official Example 1.
    assert solution.minimumSumSubarray([3, -2, 1, 4], 2, 3) == 1

    # Official Example 2.
    assert solution.minimumSumSubarray([-2, 2, -3, 1], 2, 3) == -1

    # Official Example 3.
    assert solution.minimumSumSubarray([1, 2, 3, 4], 2, 4) == 3
