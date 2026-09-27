def test_reverse_parentheses_examples(solution):
    # Example 1
    assert solution.reverseParentheses("(abcd)") == "dcba"

    # Example 2
    assert solution.reverseParentheses("(u(love)i)") == "iloveu"

    # Example 3
    assert solution.reverseParentheses("(ed(et(oc))el)") == "leetcode"


def test_reverse_parentheses_no_brackets(solution):
    # No pairs to reverse; the string is returned unchanged.
    assert solution.reverseParentheses("abc") == "abc"
