def test_has_valid_path_examples(solution):
    # Example 1
    assert solution.hasValidPath(
        [
            ["(", "(", "("],
            [")", "(", ")"],
            ["(", "(", ")"],
            ["(", "(", ")"],
        ]
    ) is True

    # Example 2
    assert solution.hasValidPath([[")", ")"], ["(", "("]] ) is False


def test_has_valid_path_single_pair(solution):
    # One-cell grids have odd path length, so they cannot be valid.
    assert solution.hasValidPath([["("]] ) is False
    # Minimal even path: "()".
    assert solution.hasValidPath([["(", ")"]]) is True
