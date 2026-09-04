def test_first_stable_index_examples(solution):
    # Example 1
    assert solution.firstStableIndex([5, 0, 1, 4], 3) == 3

    # Example 2
    assert solution.firstStableIndex([3, 2, 1], 1) == -1

    # Example 3
    assert solution.firstStableIndex([0], 0) == 0


def test_first_stable_index_single_element(solution):
    # Single element: instability is always 0, so stable for any k >= 0
    assert solution.firstStableIndex([42], 0) == 0
    assert solution.firstStableIndex([7], 100) == 0
