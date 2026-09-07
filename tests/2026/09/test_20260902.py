def test_uniform_array_examples(solution):
    # Example 1
    assert solution.uniformArray([2, 3]) is True

    # Example 2
    assert solution.uniformArray([4, 6]) is True

    # Single element is trivially uniform by keeping the value
    assert solution.uniformArray([1]) is True
