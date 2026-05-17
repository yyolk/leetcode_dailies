# https://leetcode.com/problems/count-submatrices-with-all-ones/


class Solution:
    """1504. Count Submatrices With All Ones

    Given an `m x n` binary matrix `mat`, *return the number of **submatrices** that
    have all ones*."""

    def num_submat(self, mat: list[list[int]]) -> int:
        # Get dimensions of the matrix
        m = len(mat)
        if m == 0:
            return 0
        n = len(mat[0])
        # Initialize height array for consecutive 1s in each column
        h = [0] * n
        # Initialize total count of submatrices
        ans = 0
        # Iterate over each row as the bottom row
        for r in range(m):
            # Update heights for the current row
            for j in range(n):
                if mat[r][j]:
                    h[j] += 1
                else:
                    h[j] = 0
            # Compute the sum of minimums over all subarrays of h, which gives the count for this bottom row
            # First, compute left boundaries (previous strict smaller)
            left = [-1] * n
            stack = []
            for i in range(n):
                while stack and h[stack[-1]] >= h[i]:
                    stack.pop()
                if stack:
                    left[i] = stack[-1]
                stack.append(i)
            # Compute right boundaries (next smaller or equal, but using > to handle ties)
            right = [n] * n
            stack = []
            for i in range(n - 1, -1, -1):
                while stack and h[stack[-1]] > h[i]:
                    stack.pop()
                if stack:
                    right[i] = stack[-1]
                stack.append(i)
            # Calculate the contribution for each position in h
            local = 0
            for i in range(n):
                l_dist = i - left[i]
                r_dist = right[i] - i
                local += h[i] * l_dist * r_dist
            # Add to total answer
            ans += local
        return ans

    numSubmat = num_submat
