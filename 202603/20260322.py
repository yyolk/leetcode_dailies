# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation

class Solution:
    """1886. Determine Whether Matrix Can Be Obtained By Rotation
    
    Given two n x n binary matrices mat and target, return true if it is possible
    to make mat equal to target by rotating mat in 90-degree increments (0°, 90°,
    180°, 270°), or false otherwise.
    """
    def find_rotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        # If already equal with 0° rotation
        if mat == target:
            return True

        n = len(mat)
        current = mat

        # Try rotating up to 3 times (90°, 180°, 270°)
        for _ in range(3):
            # Create new matrix rotated 90° clockwise
            rotated = [[0] * n for _ in range(n)]

            # Standard 90° clockwise rotation: new[i][j] = old[n-1-j][i]
            for i in range(n):
                for j in range(n):
                    rotated[i][j] = current[n - 1 - j][i]

            # Check if this rotation matches target
            if rotated == target:
                return True

            # Prepare for next rotation
            current = rotated

        return False

    findRotation = find_rotation