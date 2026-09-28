def test_max_depth_examples(solution):
    # Example 1
    assert solution.maxDepth("(1+(2*3)+((8)/4))+1") == 3

    # Example 2
    assert solution.maxDepth("(1)+((2))+(((3)))") == 3

    # Example 3
    assert solution.maxDepth("()(())((()()))") == 3


def test_max_depth_no_parentheses(solution):
    # A VPS with no parentheses has nesting depth 0.
    assert solution.maxDepth("1") == 0
