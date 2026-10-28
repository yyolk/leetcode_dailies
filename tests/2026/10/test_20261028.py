def test_min_cost_examples(solution):
    # Official Example 1.
    grid1 = [[1, 2], [3, 4]]
    assert solution.minCost(grid1) == 6

    # Official Example 2.
    grid2 = [[6, 7], [5, 8]]
    assert solution.minCost(grid2) == 9

    # Official Example 3.
    grid3 = [[2, 7, 5]]
    assert solution.minCost(grid3) == 0
