def test_result_array_examples(solution):
    # Example 1
    assert solution.resultArray([1, 2, 3, 4, 5], 3) == [9, 2, 4]

    # Example 2
    assert solution.resultArray([1, 2, 4, 8, 16, 32], 4) == [18, 1, 2, 0]

    # Example 3
    assert solution.resultArray([1, 1, 2, 1, 1], 2) == [9, 6]


def test_result_array_single_element(solution):
    # Single element 7, k = 5: only remainder 2
    assert solution.resultArray([7], 5) == [0, 0, 1, 0, 0]
    # k = 1: every product is 0 mod 1
    assert solution.resultArray([1], 1) == [1]
