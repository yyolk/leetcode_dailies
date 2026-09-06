def test_num_distinct_examples(solution):
    # Example 1
    assert solution.numDistinct("rabbbit", "rabbit") == 3

    # Example 2
    assert solution.numDistinct("babgbag", "bag") == 5
