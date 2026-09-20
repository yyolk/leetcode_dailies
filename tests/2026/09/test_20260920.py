def test_reverse_degree_examples(solution):
    # Example 1
    assert solution.reverseDegree("abc") == 148

    # Example 2
    assert solution.reverseDegree("zaza") == 160


def test_reverse_degree_single_letter(solution):
    # 'a' has reversed-alphabet rank 26 at 1-based index 1
    assert solution.reverseDegree("a") == 26
    # 'z' has reversed-alphabet rank 1 at 1-based index 1
    assert solution.reverseDegree("z") == 1
