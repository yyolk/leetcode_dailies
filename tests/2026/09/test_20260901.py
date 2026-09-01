def test_min_moves_examples(solution):
    # Example 1
    assert solution.minMoves(["S.", "XL"], 2) == 2

    # Example 2
    assert solution.minMoves(["LS", "RL"], 4) == 3

    # Example 3
    assert solution.minMoves(["L.S", "RXL"], 3) == -1
