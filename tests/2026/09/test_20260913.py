def test_largest_overlap_examples(solution):
    # Example 1
    assert solution.largestOverlap(
        [[1, 1, 0], [0, 1, 0], [0, 1, 0]],
        [[0, 0, 0], [0, 1, 1], [0, 0, 1]],
    ) == 3

    # Example 2
    assert solution.largestOverlap([[1]], [[1]]) == 1

    # Example 3
    assert solution.largestOverlap([[0]], [[0]]) == 0
