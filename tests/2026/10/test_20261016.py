def test_sum_counts_examples(solution):
    # Official Example 1: nums = [1,2,1] -> 15
    assert solution.sumCounts([1, 2, 1]) == 15

    # Official Example 2: nums = [2,2] -> 3
    assert solution.sumCounts([2, 2]) == 3


def test_sum_counts_single(solution):
    # Single element: one subarray with distinct count 1, square is 1.
    assert solution.sumCounts([7]) == 1
