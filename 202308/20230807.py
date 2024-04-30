# https://leetcode.com/problems/search-a-2d-matrix/


class Solution:
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        # Check if the matrix or its first row is empty
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_element = matrix[mid // n][mid % n]

            if mid_element == target:
                return True
            elif mid_element < target:
                # Update the left boundary
                left = mid + 1
            else:
                # Update the right boundary
                right = mid - 1

        return False

    searchMatrix = search_matrix