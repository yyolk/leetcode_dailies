def test_max_alternating_sum_examples(solution):
    # Official Example 1: nums = [1,2,3] -> 12
    assert solution.maxAlternatingSum([1, 2, 3]) == 12

    # Official Example 2: nums = [1,-1,2,-2,3,-3] -> 16
    assert solution.maxAlternatingSum([1, -1, 2, -2, 3, -3]) == 16


def test_max_alternating_sum_single(solution):
    # Single element: score is just its square.
    assert solution.maxAlternatingSum([5]) == 25
