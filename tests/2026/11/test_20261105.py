def test_find_the_distance_value_examples(solution):
    # Official Example 1
    assert solution.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2) == 2

    # Official Example 2
    assert solution.findTheDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3) == 2

    # Official Example 3
    assert solution.findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6) == 1
