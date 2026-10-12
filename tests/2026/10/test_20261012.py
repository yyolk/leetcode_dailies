def test_max_sum_examples(solution):
    # Official Example 1: nums = [2,6,5,8], k = 2 -> 261
    assert solution.maxSum([2, 6, 5, 8], 2) == 261

    # Official Example 2: nums = [4,5,4,7], k = 3 -> 90
    assert solution.maxSum([4, 5, 4, 7], 3) == 90


def test_max_sum_single(solution):
    # Single element: no operations needed; result is its square.
    assert solution.maxSum([5], 1) == 25
