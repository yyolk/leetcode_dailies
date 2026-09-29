# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/


class Solution:
    """2267. Check if There Is a Valid Parentheses String Path

    A parentheses string is a **non-empty** string consisting only of `'('` and
    `')'`. It is **valid** if **any** of the following conditions is **true**:

    * It is `()`.

    * It can be written as `AB` (`A` concatenated with `B`), where `A` and `B`
    are valid parentheses strings.

    * It can be written as `(A)`, where `A` is a valid parentheses string.

    You are given an `m x n` matrix of parentheses `grid`. A **valid
    parentheses string path** in the grid is a path satisfying **all** of the
    following conditions:

    * The path starts from the upper left cell `(0, 0)`.

    * The path ends at the bottom-right cell `(m - 1, n - 1)`.

    * The path only ever moves **down** or **right**.

    * The resulting parentheses string formed by the path is **valid**.

    Return `true` if there exists a **valid parentheses string path** in the
    grid. Otherwise, return `false`.

    Constraints:

    * `m == grid.length`

    * `n == grid[i].length`

    * `1 <= m, n <= 100`

    * `grid[i][j]` is either `'('` or `')'`.
    """

    def has_valid_path(self, grid: list[list[str]]) -> bool:
        """Return whether a down/right path forms a valid parentheses string."""
        rows = len(grid)
        cols = len(grid[0])
        # Path length is rows + cols - 1; valid parentheses need even length.
        if (rows + cols) % 2 == 0:
            return False
        if grid[0][0] == ")" or grid[-1][-1] == "(":
            return False

        # balances[i][j] = reachable non-negative prefix balances at (i, j).
        balances: list[list[set[int]]] = [
            [set() for _ in range(cols)] for _ in range(rows)
        ]
        start = 1 if grid[0][0] == "(" else -1
        if start < 0:
            return False
        balances[0][0].add(start)

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                delta = 1 if grid[i][j] == "(" else -1
                incoming: set[int] = set()
                if i > 0:
                    incoming |= balances[i - 1][j]
                if j > 0:
                    incoming |= balances[i][j - 1]
                # Drop any prefix that would go negative after this cell.
                balances[i][j] = {bal + delta for bal in incoming if bal + delta >= 0}

        return 0 in balances[-1][-1]

    hasValidPath = has_valid_path
