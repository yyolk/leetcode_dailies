# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/


class Solution:
    """3363. Find the Maximum Number of Fruits Collected

    There is a game dungeon comprised of `n x n` rooms arranged in a grid.

    You are given a 2D array `fruits` of size `n x n`, where `fruits[i][j]` represents
    the number of fruits in the room `(i, j)`. Three children will play in the game
    dungeon, with **initial** positions at the corner rooms `(0, 0)`, `(0, n - 1)`, and
    `(n - 1, 0)`.

    The children will make **exactly** `n - 1` moves according to the following rules to
    reach the room `(n - 1, n - 1)`:

    * The child starting from `(0, 0)` must move from their current room `(i, j)` to one
    of the rooms `(i + 1, j + 1)`, `(i + 1, j)`, and `(i, j + 1)` if the target room
    exists.

    * The child starting from `(0, n - 1)` must move from their current room `(i, j)` to
    one of the rooms `(i + 1, j - 1)`, `(i + 1, j)`, and `(i + 1, j + 1)` if the target
    room exists.

    * The child starting from `(n - 1, 0)` must move from their current room `(i, j)` to
    one of the rooms `(i - 1, j + 1)`, `(i, j + 1)`, and `(i + 1, j + 1)` if the target
    room exists.

    When a child enters a room, they will collect all the fruits there. If two or more
    children enter the same room, only one child will collect the fruits, and the room
    will be emptied after they leave.

    Return the **maximum** number of fruits the children can collect from the dungeon.
    """

    def max_collected_fruits(self, fruits: list[list[int]]) -> int:
        # Get the size of the grid n x n
        n = len(fruits)
        # Initialize the sum of fruits on the main diagonal
        sum_diag = 0
        # Loop through each index i from 0 to n-1
        for i in range(n):
            # Add the fruit at position (i, i) to the sum
            sum_diag += fruits[i][i]

        # Define a function to compute extra fruits for child B starting from top-right
        # For child B (top-right)
        def get_extra_B() -> int:
            # Define negative infinity for initialization
            INF = float('-inf')
            # Create a 2D DP table of size n x n initialized with -inf
            dp = [[INF] * n for _ in range(n)]
            # Starting column for child B
            j_start = n - 1
            # Initialize DP for row 0, column j_start; avoid double-counting if on diagonal
            dp[0][j_start] = fruits[0][j_start] if 0 != j_start else 0
            # Loop through each row i from 1 to n-1
            for i in range(1, n):
                # Loop through each column j from 0 to n-1
                for j in range(n):
                    # Initialize max from previous row
                    max_prev = INF
                    # Check possible moves: left, same, right
                    for d in [-1, 0, 1]:
                        # Calculate previous column
                        prev_j = j + d
                        # Check if previous column is within bounds
                        if 0 <= prev_j < n:
                            # Update max_prev with the max from possible previous positions
                            max_prev = max(max_prev, dp[i - 1][prev_j])
                    # If there is a valid previous max
                    if max_prev != INF:
                        # Add fruits at current position if not on diagonal
                        add = fruits[i][j] if i != j else 0
                        # Update DP table with max_prev plus add
                        dp[i][j] = max_prev + add
            # Return the value at bottom-right for child B, converted to int
            return int(dp[n - 1][n - 1])  # Convert to int if needed

        # Define a function to compute extra fruits for child C starting from bottom-left
        # For child C (bottom-left)
        def get_extra_C() -> int:
            # Define negative infinity for initialization
            INF = float('-inf')
            # Create a 2D DP table of size n x n initialized with -inf
            dp = [[INF] * n for _ in range(n)]
            # Starting row for child C
            r_start = n - 1
            # Initialize DP for column 0, row r_start; avoid double-counting if on diagonal
            dp[0][r_start] = fruits[r_start][0] if r_start != 0 else 0
            # Loop through each column j_col from 1 to n-1
            for j_col in range(1, n):
                # Loop through each row r from 0 to n-1
                for r in range(n):
                    # Initialize max from previous column
                    max_prev = INF
                    # Check possible moves: up, same, down (but adjusted for row direction)
                    for d in [-1, 0, 1]:
                        # Calculate previous row
                        prev_r = r + d
                        # Check if previous row is within bounds
                        if 0 <= prev_r < n:
                            # Update max_prev with the max from possible previous positions
                            max_prev = max(max_prev, dp[j_col - 1][prev_r])
                    # If there is a valid previous max
                    if max_prev != INF:
                        # Add fruits at current position if not on diagonal
                        add = fruits[r][j_col] if r != j_col else 0
                        # Update DP table with max_prev plus add
                        dp[j_col][r] = max_prev + add
            # Return the value at bottom-right for child C, converted to int
            return int(dp[n - 1][n - 1])

        # Return the total: diagonal sum plus extras from B and C
        return sum_diag + get_extra_B() + get_extra_C()

    maxCollectedFruits = max_collected_fruits
