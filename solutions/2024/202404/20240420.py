# https://leetcode.com/problems/find-all-groups-of-farmland/


class Solution:
    """1992. Find All Groups of Farmland

    You are given a **0-indexed** `m x n` binary matrix `land` where a `0` represents a
    hectare of forested land and a `1` represents a hectare of farmland.

    To keep the land organized, there are designated rectangular areas of hectares that
    consist **entirely** of farmland. These rectangular areas are called **groups**. No
    two groups are adjacent, meaning farmland in one group is **not** four-directionally
    adjacent to another farmland in a different group.

    `land` can be represented by a coordinate system where the top left corner of `land`
    is `(0, 0)` and the bottom right corner of `land` is `(m-1, n-1)`. Find the
    coordinates of the top left and bottom right corner of each **group** of farmland. A
    **group** of farmland with a top left corner at `(r1, c1)` and a bottom right corner
    at `(r2, c2)` is represented by the 4-length array `[r1, c1, r2, c2].`

    Return *a 2D array containing the 4-length arrays described above for each **group**
    of farmland in* `land`*. If there are no groups of farmland, return an empty array.
    You may return the answer in **any order***.

    """

    def find_farmland(self, land: list[list[int]]) -> list[list[int]]:
        # Get the number of rows and columns
        num_rows, num_cols = len(land), len(land[0])
        # Initialize list to store farmland rectangles
        farmlands = []

        for i in range(num_rows):  # Iterate over rows
            for j in range(num_cols):  # Iterate over columns
                # Check if (i, j) is the start of a new farmland rectangle
                if (
                    land[i][j] == 1
                    and (i == 0 or land[i - 1][j] == 0)
                    and (j == 0 or land[i][j - 1] == 0)
                ):
                    bottom_row = i
                    right_col = j

                    # Expand down to find the bottom boundary
                    while bottom_row + 1 < num_rows and land[bottom_row + 1][j] == 1:
                        bottom_row += 1
                    # Expand right to find the right boundary
                    while right_col + 1 < num_cols and land[i][right_col + 1] == 1:
                        right_col += 1

                    # Add farmland rectangle coordinates to the result
                    farmlands.append([i, j, bottom_row, right_col])

        return farmlands

    findFarmland = find_farmland
