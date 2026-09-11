def test_total_numbers_examples(solution):
    # Example 1
    assert solution.totalNumbers([1, 2, 3, 4]) == 12

    # Example 2
    assert solution.totalNumbers([0, 2, 2]) == 2

    # Example 3
    assert solution.totalNumbers([6, 6, 6]) == 1

    # Example 4
    assert solution.totalNumbers([1, 3, 5]) == 0
