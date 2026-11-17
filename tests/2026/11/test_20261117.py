def test_minimum_changes_examples(solution):
    # Official Example 1.
    assert solution.minimumChanges("abcac", 2) == 1

    # Official Example 2.
    assert solution.minimumChanges("abcdef", 2) == 2

    # Official Example 3.
    assert solution.minimumChanges("aabbaa", 3) == 0
