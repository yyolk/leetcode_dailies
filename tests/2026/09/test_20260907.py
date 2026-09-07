def test_distinct_subseq_ii_examples(solution):
    # Example 1
    assert solution.distinctSubseqII("abc") == 7

    # Example 2
    assert solution.distinctSubseqII("aba") == 6

    # Example 3
    assert solution.distinctSubseqII("aaa") == 3
