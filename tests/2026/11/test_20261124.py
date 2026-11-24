def test_max_length_examples(solution):
    # Official Example 1.
    assert solution.maxLength([1, 2, 1, 2, 1, 1, 1]) == 5

    # Official Example 2.
    assert solution.maxLength([2, 3, 4, 5, 6]) == 3

    # Official Example 3.
    assert solution.maxLength([1, 2, 3, 1, 4, 5, 1]) == 5
