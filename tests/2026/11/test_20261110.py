def test_climb_stairs_examples(solution):
    # Official Example 1.
    assert solution.climbStairs(4, [1, 2, 3, 4]) == 13

    # Official Example 2.
    assert solution.climbStairs(4, [5, 1, 6, 2]) == 11

    # Official Example 3.
    assert solution.climbStairs(3, [9, 8, 3]) == 12

    # Trivial single-step case (direct jump of 1).
    assert solution.climbStairs(1, [5]) == 6
