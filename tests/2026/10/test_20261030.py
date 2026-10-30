def test_shortest_path_examples(solution):
    # Official Example 1.
    assert solution.shortestPath(3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 1) == 3

    # Official Example 2.
    assert solution.shortestPath(3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 2) == 2

    # Official Example 3.
    assert solution.shortestPath(3, [[0, 1, 1], [1, 2, 1]], "aaa", 2) == -1

    # Trivial single-node identity case (cost 0).
    assert solution.shortestPath(1, [], "a", 1) == 0
