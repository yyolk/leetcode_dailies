def test_sum_of_squares_examples(solution):
    # Official Example 1: nums = [1,2,3,4] -> 21
    assert solution.sumOfSquares([1, 2, 3, 4]) == 21

    # Official Example 2: nums = [2,7,1,19,18,3] -> 63
    assert solution.sumOfSquares([2, 7, 1, 19, 18, 3]) == 63


def test_sum_of_squares_single(solution):
    # Single element is always special (1 divides 1).
    assert solution.sumOfSquares([5]) == 25
