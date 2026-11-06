def test_count_servers_examples(solution):
    # Official Example 1
    assert solution.countServers(3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11]) == [1, 2]

    # Official Example 2
    assert solution.countServers(3, [[2, 4], [2, 1], [1, 2], [3, 1]], 2, [3, 4]) == [
        0,
        1,
    ]
