def test_min_add_to_make_valid_examples(solution):
    # Example 1
    assert solution.minAddToMakeValid("())") == 1

    # Example 2
    assert solution.minAddToMakeValid("(((") == 3


def test_min_add_to_make_valid_already_valid(solution):
    # A matched pair needs no insertions.
    assert solution.minAddToMakeValid("()") == 0
