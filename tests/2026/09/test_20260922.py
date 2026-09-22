def test_result_array_examples(solution):
    # Example 1
    assert solution.resultArray(
        [1, 2, 3, 4, 5], 3, [[2, 2, 0, 2], [3, 3, 3, 0], [0, 1, 0, 1]]
    ) == [2, 2, 2]

    # Example 2
    assert solution.resultArray(
        [1, 2, 4, 8, 16, 32], 4, [[0, 2, 0, 2], [0, 2, 0, 1]]
    ) == [1, 0]

    # Example 3
    assert solution.resultArray([1, 1, 2, 1, 1], 2, [[2, 1, 0, 1]]) == [5]


def test_result_array_single_element(solution):
    # After setting [7], start=0, x=2: product 7 % 5 == 2, one prefix
    assert solution.resultArray([7], 5, [[0, 7, 0, 2]]) == [1]
    # k = 1: every product is 0 mod 1
    assert solution.resultArray([1], 1, [[0, 1, 0, 0]]) == [1]
