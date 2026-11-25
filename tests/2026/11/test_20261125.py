def test_smallest_unique_subarray_examples(solution):
    # Official Example 1.
    assert solution.smallestUniqueSubarray([3, 3, 3]) == 3

    # Official Example 2.
    assert solution.smallestUniqueSubarray([2, 1, 2, 3, 3]) == 1

    # Official Example 3.
    assert solution.smallestUniqueSubarray([1, 1, 2, 2, 1]) == 2
