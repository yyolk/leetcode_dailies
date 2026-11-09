def test_busiest_servers_examples(solution):
    # Official Example 1.
    assert solution.busiestServers(3, [1, 2, 3, 4, 5], [5, 2, 3, 3, 3]) == [1]

    # Official Example 2.
    assert solution.busiestServers(3, [1, 2, 3, 4], [1, 2, 1, 2]) == [0]

    # Official Example 3.
    assert sorted(solution.busiestServers(3, [1, 2, 3], [10, 12, 11])) == [0, 1, 2]
