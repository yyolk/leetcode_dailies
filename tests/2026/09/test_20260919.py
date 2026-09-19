def test_check_overlap_examples(solution):
    assert solution.checkOverlap(1, 0, 0, 1, -1, 3, 1) is True
    assert solution.checkOverlap(1, 1, 1, 1, -3, 2, -1) is False
    assert solution.checkOverlap(1, 0, 0, -1, 0, 0, 1) is True


def test_check_overlap_center_inside_rectangle(solution):
    # Circle center is inside the rectangle, so they overlap for any radius.
    assert solution.checkOverlap(1, 0, 0, -2, -2, 2, 2) is True
