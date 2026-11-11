def test_minimum_cost_examples(solution):
    # Official Example 1.
    assert solution.minimumCost(3, 2, 1, 3, 2) == 3

    # Official Example 2.
    assert solution.minimumCost(5, 4, 15, 2, 3) == 22

    # Official Example 3.
    assert solution.minimumCost(5, 4, 15, 0, 0) == 0

    # Trivial case: only type-1 items needed.
    assert solution.minimumCost(7, 9, 20, 4, 0) == 28
