def test_remove_invalid_parentheses_examples(solution):
    # Example 1
    assert set(solution.removeInvalidParentheses("()())()")) == {
        "(())()",
        "()()()",
    }

    # Example 2
    assert set(solution.removeInvalidParentheses("(a)())()")) == {
        "(a())()",
        "(a)()()",
    }

    # Example 3
    assert solution.removeInvalidParentheses(")(") == [""]


def test_remove_invalid_parentheses_already_valid(solution):
    # A matched pair is already valid, so nothing is removed.
    assert solution.removeInvalidParentheses("()") == ["()"]
