# https://leetcode.com/problems/01-matrix/
from collections import deque


class Solution:
    """542. 01 Matrix

    Given an `m x n` binary matrix `mat`, return *the distance of the nearest* `0` *for
    each cell*.

    The distance between two adjacent cells is `1`.
    """

    def update_matrix(self, mat: list[list[int]]) -> list[list[int]]:
        """Computes the distance of the nearest 0 for each cell in the binary matrix.

        Given an `m x n` binary matrix `mat`, this method calculates the distance from
        each cell to the nearest cell with the value 0 using a breadth-first search (BFS)
        approach. The distance between adjacent cells is considered to be 1.

        Args:
            mat: A 2D binary matrix represented as a list of lists, where `mat[i][j]`
            is either 0 or 1.

        Returns:
            A 2D matrix of the same dimensions as the input matrix, where each cell
            contains the distance to the nearest 0 in the input matrix.

        Example:
            Given the input matrix:
            [
                [0, 0, 0],
                [0, 1, 0],
                [1, 1, 1]
            ]

            The output will be:
            [
                [0, 0, 0],
                [0, 1, 0],
                [1, 2, 1]
            ]
        """
        if not mat:
            return mat
        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque()

        # Initialize the queue with all cells with value 0 and mark otthers as -1.
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1

        while queue:
            i, j = queue.popleft()

            # Explore the neighbors of (i, j).
            for dx, dy in directions:
                x, y = i + dx, j + dy

                if 0 <= x < m and 0 <= y < n and mat[x][y] == -1:
                    # Update the distance to the nearest 0 cell.
                    mat[x][y] = mat[i][j] + 1
                    queue.append((x, y))

        return mat

    updateMatrix = update_matrix
