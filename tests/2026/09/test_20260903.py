def test_uniform_array_examples(solution):
    # Example 1
    assert solution.uniformArray([1, 4, 7]) is True

    # Example 2
    assert solution.uniformArray([2, 3]) is False

    # Example 3
    assert solution.uniformArray([4, 6]) is True


def test_uniform_array_single(solution):
    # Single element must keep its value and is trivially uniform
    assert solution.uniformArray([1]) is True
    assert solution.uniformArray([2]) is True
