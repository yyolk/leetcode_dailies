def test_num_of_subarrays_examples(solution):
    # Official Example 1.
    assert solution.numOfSubarrays([1, 3, 5]) == 4

    # Official Example 2.
    assert solution.numOfSubarrays([2, 4, 6]) == 0

    # Official Example 3.
    assert solution.numOfSubarrays([1, 2, 3, 4, 5, 6, 7]) == 16

    # Trivial single-element cases (odd -> 1, even -> 0).
    assert solution.numOfSubarrays([1]) == 1
    assert solution.numOfSubarrays([2]) == 0
