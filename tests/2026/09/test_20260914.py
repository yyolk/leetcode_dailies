def test_is_rectangle_overlap_examples(solution):
    # Example 1
    assert solution.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]) is True

    # Example 2
    assert solution.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]) is False

    # Example 3
    assert solution.isRectangleOverlap([0, 0, 1, 1], [2, 2, 3, 3]) is False
