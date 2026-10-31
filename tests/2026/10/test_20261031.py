def test_unique_paths_examples(solution):
    # Official Example 1.
    assert solution.uniquePaths([[0, 1, 0], [0, 0, 1], [1, 0, 0]]) == 5

    # Official Example 2.
    assert solution.uniquePaths([[0, 0], [0, 0]]) == 2

    # Official Example 3.
    assert solution.uniquePaths([[0, 1, 1], [1, 1, 0]]) == 1
