def test_max_sum_of_squares_examples(solution):
    # Official Example 1: num = 2, sum = 3 -> "30"
    assert solution.maxSumOfSquares(2, 3) == "30"

    # Official Example 2: num = 2, sum = 17 -> "98"
    assert solution.maxSumOfSquares(2, 17) == "98"

    # Official Example 3: num = 1, sum = 10 -> ""
    assert solution.maxSumOfSquares(1, 10) == ""


def test_max_sum_of_squares_single_digit(solution):
    # Single digit that fits exactly.
    assert solution.maxSumOfSquares(1, 5) == "5"
