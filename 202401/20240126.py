# https://leetcode.com/problems/out-of-boundary-paths/


class Solution:
    """576. Out of Boundary Paths

    There is an `m x n` grid with a ball. The ball is initially at the position
    `[start_row, start_column]`. You are allowed to move the ball to one of the four
    adjacent cells in the grid (possibly out of the grid crossing the grid boundary).
    You can apply **at most** `max_move` moves to the ball.

    Given the five integers `m`, `n`, `max_move`, `start_row`, `start_column`, return
    the number of paths to move the ball out of the grid boundary. Since the answer can
    be very large, return it **modulo** `109 + 7`.
    """

    def find_paths(
        self, m: int, n: int, max_move: int, start_row: int, start_column: int
    ) -> int:
        ...

    findPaths = find_paths
