# https://leetcode.com/problems/snakes-and-ladders/
from collections import deque


class Solution:
    """909. Snakes and Ladders

    You are given an `n x n` integer matrix `board` where the cells are labeled from `1`
    to `n2` in a [**Boustrophedon style**](https://en.wikipedia.org/wiki/Boustrophedon)
    starting from the bottom left of the board (i.e. `board[n - 1][0]`) and alternating
    direction each row.

    You start on square `1` of the board. In each move, starting from square `curr`, do
    the following:

    * Choose a destination square `next` with a label in the range `[curr + 1, min(curr
    + 6, n2)]`.

      + This choice simulates the result of a standard **6-sided die roll**: i.e., there
    are always at most 6 destinations, regardless of the size of the board.

    * If `next` has a snake or ladder, you **must** move to the destination of that
    snake or ladder. Otherwise, you move to `next`.

    * The game ends when you reach the square `n2`.

    A board square on row `r` and column `c` has a snake or ladder if `board[r][c] !=
    -1`. The destination of that snake or ladder is `board[r][c]`. Squares `1` and `n2`
    are not the starting points of any snake or ladder.

    Note that you only take a snake or ladder at most once per dice roll. If the
    destination to a snake or ladder is the start of another snake or ladder, you do
    **not** follow the subsequent snake or ladder.

    * For example, suppose the board is `[[-1,4],[-1,3]]`, and on the first move, your
    destination square is `2`. You follow the ladder to square `3`, but do **not**
    follow the subsequent ladder to `4`.

    Return *the least number of dice rolls required to reach the square* `n2`*. If it is
    not possible to reach the square, return* `-1`."""

    def snakes_and_ladders(self, board: list[list[int]]) -> int:
        n = len(board)

        # Helper function to convert label k to (row, col) position
        def label_to_pos(k):
            r = n - 1 - (k - 1) // n
            if ((k - 1) // n) % 2 == 0:
                c = (k - 1) % n
            else:
                c = n - 1 - (k - 1) % n
            return r, c

        # BFS setup
        queue = deque([(1, 0)])  # (current square, moves)
        visited = set([1])

        # BFS loop
        while queue:
            curr, moves = queue.popleft()
            if curr == n * n:
                return moves

            # Try all possible dice rolls (1 to 6)
            for next_label in range(curr + 1, min(curr + 7, n * n + 1)):
                r, c = label_to_pos(next_label)
                # If there's a snake or ladder, go to its destination; otherwise, stay at next_label
                final = board[r][c] if board[r][c] != -1 else next_label
                if final not in visited:
                    visited.add(final)
                    queue.append((final, moves + 1))

        return -1

    snakesAndLadders = snakes_and_ladders
