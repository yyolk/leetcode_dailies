def test_count_servers_examples(solution):
    # Official Example 1.
    grid1 = [[1, 0], [0, 1]]
    assert solution.countServers(grid1) == 0

    # Official Example 2.
    grid2 = [[1, 0], [1, 1]]
    assert solution.countServers(grid2) == 3

    # Official Example 3.
    grid3 = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    assert solution.countServers(grid3) == 4


def test_count_servers_trivial(solution):
    # Single server is isolated.
    grid = [[1]]
    assert solution.countServers(grid) == 0

    # No servers.
    grid_empty = [[0, 0], [0, 0]]
    assert solution.countServers(grid_empty) == 0
