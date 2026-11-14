def test_count_non_decreasing_subarrays_examples(solution):
    # Official Example 1.
    assert solution.countNonDecreasingSubarrays([6, 3, 1, 2, 4, 4], 7) == 17

    # Official Example 2.
    assert solution.countNonDecreasingSubarrays([6, 3, 1, 3, 6], 4) == 12
