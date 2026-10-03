def test_longest_valid_parentheses_examples(solution):
    # Example 1
    assert solution.longestValidParentheses("(()") == 2

    # Example 2
    assert solution.longestValidParentheses(")()())") == 4

    # Example 3
    assert solution.longestValidParentheses("") == 0


def test_longest_valid_parentheses_single_pair(solution):
    # One matched pair is a valid substring of length 2.
    assert solution.longestValidParentheses("()") == 2
