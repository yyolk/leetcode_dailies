def test_smallest_index_examples(solution):
    # Example 1
    assert solution.smallestIndex([1, 3, 2]) == 2

    # Example 2
    assert solution.smallestIndex([1, 10, 11]) == 1

    # Example 3
    assert solution.smallestIndex([1, 2, 3]) == -1


def test_smallest_index_single_zero(solution):
    # Digit sum of 0 is 0, matching index 0.
    assert solution.smallestIndex([0]) == 0
