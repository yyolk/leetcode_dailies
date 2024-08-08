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
    ) -> list[list[int]]:
        result = [[r_start, c_start]]
        if rows * cols == 1:
            return result

        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Start facing east (right)
        d = 0  
        
        steps = 0
        r, c = r_start, c_start

        while len(result) < rows * cols:
            steps += 1
            for _ in range(2):
                for _ in range(steps):
                    r += directions[d][0]
                    c += directions[d][1]
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                    if len(result) == rows * cols:
                        return result
                # Turn 90 degrees clockwise                        
                d = (d + 1) % 4

        return result
    
    spiralMatrixIII = spiral_matrix_i_i_i
