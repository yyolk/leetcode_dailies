def test_min_moves_examples(solution):
    # Official Example 1.
    assert solution.minMoves([1, 2, 3]) == 3

    # Official Example 2.
    assert solution.minMoves([1, 1, 1]) == 0

    # Single-element identity case.
    assert solution.minMoves([42]) == 0
