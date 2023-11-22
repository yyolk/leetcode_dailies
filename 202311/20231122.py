# https://leetcode.com/problems/diagonal-traverse-ii/
import heapq


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
        # Create a min heap.
        heap = []
        # Create the result list.
        result = []

        # Push elements into the heap with the tuple:
        #   (sum of indices, -row index, element).
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                heapq.heappush(heap, (i + j, -i, nums[i][j]))

        # Pop elements from the heap and append them to the result list.
        while heap:
            _, _, element = heapq.heappop(heap)
            result.append(element)

        return result

    findDiagonalOrder = find_diagonal_order
