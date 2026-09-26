def test_evaluate_examples(solution):
    # Example 1
    assert (
        solution.evaluate(
            "(name)is(age)yearsold",
            [["name", "bob"], ["age", "two"]],
        )
        == "bobistwoyearsold"
    )

    # Example 2
    assert solution.evaluate("hi(name)", [["a", "b"]]) == "hi?"

    # Example 3
    assert solution.evaluate("(a)(a)(a)aaa", [["a", "yes"]]) == "yesyesyesaaa"


def test_evaluate_no_brackets(solution):
    # No pairs to replace; the string is returned unchanged.
    assert solution.evaluate("hello", []) == "hello"
