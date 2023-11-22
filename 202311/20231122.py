# https://leetcode.com/problems/diagonal-traverse-ii/
from collections import deque


class Solution:
    """1424. Diagonal Traverse II

    Given a 2D integer array `nums`, return *all elements of* `nums` *in diagonal order
    as shown in the below images*.
    """

    def find_diagonal_order(self, nums: list[list[int]]) -> list[int]:
        """Returns all elements from nums in diagonal order.

        Args:
            nums: Input 2D integer array of input elements.

        Returns:
            Integer array of elements starting from top left to bottom right of
            elements in diagonal order.
        """
        # Create the result list.
        result = []
        # Create the double-ended queue
        dq = deque([[0, 0]])
        n = len(nums)

        while dq:
            i, j = dq.popleft()
            result.append(nums[i][j])
            # If we are at the beginning of a row and there is a row below,
            # add the element below.
            if j == 0 and i + 1 < n:
                dq.append([i + 1, j])
            # If there is a column to the right, add the element to the right.
            if j + 1 < len(nums[i]):
                dq.append([i, j + 1])

        return result

    findDiagonalOrder = find_diagonal_order
