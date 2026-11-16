def test_digit_sum_examples(solution):
    # Official Example 1.
    assert solution.digitSum("11111222223", 3) == "135"

    # Official Example 2.
    assert solution.digitSum("00000000", 3) == "000"

    # Trivial case where length is already <= k (identity).
    assert solution.digitSum("123", 5) == "123"
