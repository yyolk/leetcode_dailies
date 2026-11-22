def test_check_string_examples(solution):
    # Official Example 1.
    assert solution.checkString("aaabbb") is True

    # Official Example 2.
    assert solution.checkString("abab") is False

    # Official Example 3.
    assert solution.checkString("bbb") is True
