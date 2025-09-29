# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/


class Solution:
    """1039. Minimum Score Triangulation of Polygon

    You have a convex `n`-sided polygon where each vertex has an integer value. You are
    given an integer array `values` where `values[i]` is the value of the `ith` vertex
    in **clockwise order**.

    **Polygon** **triangulation** is a process where you divide a polygon into a set of
    triangles and the vertices of each triangle must also be vertices of the original
    polygon. Note that no other shapes other than triangles are allowed in the division.
    This process will result in `n - 2` triangles.

    You will **triangulate** the polygon. For each triangle, the *weight* of that
    triangle is the product of the values at its vertices. The total score of the
    triangulation is the sum of these *weights* over all `n - 2` triangles.

    Return the *minimum possible score* that you can achieve with
    some**triangulation**of the polygon."""

    def min_score_triangulation(self, values: list[int]) -> int:
        # Get the number of vertices
        n = len(values)
        # Handle edge case for n < 3, though problem assumes n >= 3
        if n < 3:
            return 0
        # Initialize DP table where dp[i][j] is min cost to triangulate vertices i to j
        dp = [[0] * n for _ in range(n)]
        # Iterate over increasing sub-polygon lengths (from 3 vertices up)
        for length in range(2, n):
            # For each possible starting index i for this length
            for i in range(n - length):
                # Compute ending index j
                j = i + length
                # Start with infinite cost for minimization
                dp[i][j] = float('inf')
                # Try every possible split point k between i and j
                for k in range(i + 1, j):
                    # Cost = sub-cost i to k + sub-cost k to j + triangle i-k-j product
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[k] * values[j])
        # Return min cost for full polygon (vertices 0 to n-1)
        return dp[0][n - 1]

    minScoreTriangulation = min_score_triangulation
