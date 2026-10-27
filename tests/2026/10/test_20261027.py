def _count_paths(grid: list[str]) -> int:
    """Count right/down paths from top-left to bottom-right."""
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    if grid[0][0] == "#" or grid[m - 1][n - 1] == "#":
        return 0
    # DP: number of ways to reach each free cell.
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "#" or (i == 0 and j == 0):
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    return dp[m - 1][n - 1]


def test_create_grid_examples(solution):
    # Official Example 1 input. Any correct grid is accepted; we verify
    # exactly one valid path exists (and start/end are free).
    result1 = solution.createGrid(2, 3)
    assert len(result1) == 2 and all(len(row) == 3 for row in result1)
    assert result1[0][0] == "." and result1[-1][-1] == "."
    assert _count_paths(result1) == 1

    # Official Example 2 input.
    result2 = solution.createGrid(3, 3)
    assert len(result2) == 3 and all(len(row) == 3 for row in result2)
    assert result2[0][0] == "." and result2[-1][-1] == "."
    assert _count_paths(result2) == 1

    # Official Example 3 input (and output is unique).
    result3 = solution.createGrid(1, 4)
    assert result3 == ["...."]
    assert _count_paths(result3) == 1

    # Also confirm the official sample outputs themselves have exactly one path.
    assert _count_paths(["..#", "#.."]) == 1
    assert _count_paths(["..#", "#..", "##."]) == 1


def test_create_grid_single_cell(solution):
    # Trivial identity: 1x1 must be a single free cell.
    result = solution.createGrid(1, 1)
    assert result == ["."]
    assert _count_paths(result) == 1
