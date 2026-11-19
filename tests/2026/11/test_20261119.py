def test_minimize_sum_examples(solution):
    # Official Example 1.
    assert solution.minimizeSum([1, 4, 7, 8, 5]) == 3

    # Official Example 2.
    assert solution.minimizeSum([1, 4, 3]) == 0

    # Trivial all-equal case (obvious from spec).
    assert solution.minimizeSum([5, 5, 5]) == 0
