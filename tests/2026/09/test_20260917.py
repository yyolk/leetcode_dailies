def test_min_sum_of_lengths_examples(solution):
    # Example 1
    assert solution.minSumOfLengths([3, 2, 2, 4, 3], 3) == 2

    # Example 2
    assert solution.minSumOfLengths([7, 3, 4, 7], 7) == 2

    # Example 3
    assert solution.minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6) == -1


def test_min_sum_of_lengths_single_element(solution):
    # Only one subarray can exist, so two non-overlapping ones are impossible.
    assert solution.minSumOfLengths([3], 3) == -1
