def test_min_moves_examples(solution):
    assert solution.minMoves([2, 1, 3]) == 3
    assert solution.minMoves([4, 4, 5]) == 2


def test_min_moves_single_element(solution):
    assert solution.minMoves([7]) == 0


def test_min_moves_all_equal(solution):
    assert solution.minMoves([5, 5, 5]) == 0
