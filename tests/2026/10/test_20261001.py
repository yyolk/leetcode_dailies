def test_is_valid_examples(solution):
    # Example 1
    assert solution.isValid("()") is True

    # Example 2
    assert solution.isValid("()[]{}") is True

    # Example 3
    assert solution.isValid("(]") is False

    # Example 4
    assert solution.isValid("([])") is True

    # Example 5
    assert solution.isValid("([)]") is False


def test_is_valid_single_bracket(solution):
    # Length 1 cannot pair an opener with a closer.
    assert solution.isValid("(") is False
    assert solution.isValid(")") is False
