# https://leetcode.com/problems/count-servers-that-communicate/


class Solution:
    """1267. Count Servers that Communicate

    You are given a map of a server center, represented as a `m * n` integer matrix
    `grid`, where 1 means that on that cell there is a server and 0 means that it is no
    server. Two servers are said to communicate if they are on the same row or on the
    same column.



    Return the number of servers that communicate with any other server."""

    def count_servers(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        row_count = [0] * m
        col_count = [0] * n

        # Count servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # Count servers that can communicate
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    result += 1

        return result

    countServers = count_servers
