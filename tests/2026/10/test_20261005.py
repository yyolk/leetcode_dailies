def test_score_of_parentheses_examples(solution):
    # Example 1
    assert solution.scoreOfParentheses("()") == 1

    # Example 2
    assert solution.scoreOfParentheses("(())") == 2

    # Example 3
    assert solution.scoreOfParentheses("()()") == 2
