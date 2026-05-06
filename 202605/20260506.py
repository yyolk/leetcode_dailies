# https://leetcode.com/problems/rotating-the-box/

class Solution:
    """1861. Rotating the Box

    You are given an m x n matrix of characters boxGrid representing a side-view
    of a box. Each cell of the box is one of the following: A stone '#', a
    stationary obstacle '*', empty '.'.

    The box is rotated 90 degrees clockwise, causing some of the stones to fall
    due to gravity. Each stone falls down until it lands on an obstacle, another
    stone, or the bottom of the box. Gravity does not affect the obstacles'
    positions, and the inertia from the box's rotation does not affect the
    stones' horizontal positions.

    It is guaranteed that each stone in boxGrid rests on an obstacle, another
    stone, or the bottom of the box.

    Return an n x m matrix representing the box after the rotation described
    above.
    """
    def rotate_the_box(self, box_grid: list[list[str]]) -> list[list[str]]:
        m = len(box_grid)
        n = len(box_grid[0])

        # create the rotated grid (n rows x m columns)
        new_grid = [["." for _ in range(m)] for _ in range(n)]

        # perform 90 degree clockwise rotation: old[i][j] -> new[j][m-1-i]
        for i in range(m):
            for j in range(n):
                new_grid[j][m - 1 - i] = box_grid[i][j]

        # simulate gravity in each column of new grid
        # stones fall down (towards higher row indices)
        for col in range(m):
            write = n - 1
            for r in range(n - 1, -1, -1):
                if new_grid[r][col] == "*":
                    # reset write position above the obstacle
                    write = r - 1
                elif new_grid[r][col] == "#":
                    # move stone to the lowest available position
                    new_grid[r][col] = "."
                    new_grid[write][col] = "#"
                    write -= 1

        return new_grid

    rotateTheBox = rotate_the_box