# https://leetcode.com/problems/spiral-matrix-iii/


class Solution:
    """885. Spiral Matrix III

    You start at the cell `(r_start, c_start)` of an `rows x cols` grid facing east. The
    northwest corner is at the first row and column in the grid, and the southeast
    corner is at the last row and column.

    You will walk in a clockwise spiral shape to visit every position in this grid.
    Whenever you move outside the grid's boundary, we continue our walk outside the grid
    (but may return to the grid boundary later.). Eventually, we reach all `rows * cols`
    spaces of the grid.

    Return *an array of coordinates representing the positions of the grid in the order
    you visited them*.

    """

    def spiral_matrix_i_i_i(
        self, rows: int, cols: int, r_start: int, c_start: int
    ) -> list[list[int]]: ...

    spiralMatrixIII = spiral_matrix_i_i_i
