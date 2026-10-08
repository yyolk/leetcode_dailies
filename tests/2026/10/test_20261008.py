def test_remove_outer_parentheses_examples(solution):
    # Example 1: "(()())" + "(())" -> "()()" + "()"
    assert solution.removeOuterParentheses("(()())(())") == "()()()"

    # Example 2: "(()())" + "(())" + "(()(()))" -> "()()" + "()" + "()(())"
    assert solution.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"

    # Example 3: "()" + "()" -> "" + ""
    assert solution.removeOuterParentheses("()()") == ""


def test_remove_outer_parentheses_single_primitive(solution):
    # A single pair is one primitive, so removing its outer pair leaves nothing.
    assert solution.removeOuterParentheses("()") == ""
