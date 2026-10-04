def test_check_valid_string_examples(solution):
    # Example 1
    assert solution.checkValidString("()") is True

    # Example 2
    assert solution.checkValidString("(*)") is True

    # Example 3
    assert solution.checkValidString("(*))") is True


def test_check_valid_string_single_close(solution):
    # A lone closer has no matching opener.
    assert solution.checkValidString(")") is False
