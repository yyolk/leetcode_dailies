def test_generate_parenthesis_examples(solution):
    # Example 1. Order is not part of the contract.
    assert sorted(solution.generateParenthesis(3)) == sorted(
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
    )

    # Example 2
    assert solution.generateParenthesis(1) == ["()"]
