def test_min_changes_examples(solution):
    # Official Example 1.
    assert solution.minChanges("1001") == 2

    # Official Example 2.
    assert solution.minChanges("10") == 1

    # Official Example 3.
    assert solution.minChanges("0000") == 0
