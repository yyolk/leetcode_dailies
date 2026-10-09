def test_min_insertions_examples(solution):
    # Example 1: first '(' is short one ')', so insert one ')' at the end.
    assert solution.minInsertions("(()))") == 1

    # Example 2: already balanced as '(' + '))'.
    assert solution.minInsertions("())") == 0

    # Example 3: insert '(' for the first '))' and '))' for the last '('.
    assert solution.minInsertions("))())(") == 3


def test_min_insertions_single_open(solution):
    # A single '(' needs two closing parens.
    assert solution.minInsertions("(") == 2
