# https://leetcode.com/problems/count-servers-that-communicate/


class Solution:
    """1267. Count Servers that Communicate

    You are given a map of a server center, represented as an m * n integer
    matrix grid, where 1 means that on that cell there is a server and 0 means
    that it is no server. Two servers are said to communicate if they are on
    the same row or on the same column.

    Return the number of servers that communicate with any other server.

    Constraints:

    * m == grid.length

    * n == grid[i].length

    * 1 <= m <= 250

    * 1 <= n <= 250

    * grid[i][j] == 0 or 1
    """

    def count_servers(self, grid: list[list[int]]) -> int:
        """Count servers that share a row or column with another server.

        Args:
            grid: m x n matrix with 0/1 indicating servers.

        Returns:
            Number of non-isolated servers.
        """
        # Empty grid has no servers.
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        # Count servers in each row and each column.
        row_counts = [sum(row) for row in grid]
        col_counts = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        # A server communicates if its row or column has more than one server.
        communicating = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (
                    row_counts[i] > 1 or col_counts[j] > 1
                ):
                    communicating += 1

        return communicating

    countServers = count_servers
