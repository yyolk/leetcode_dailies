# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/


class Solution:
    """1574. Shortest Subarray to be Removed to Make Array Sorted

    Given an integer array `arr`, remove a subarray (can be empty) from `arr` such that
    the remaining elements in `arr` are **non\\-decreasing**.

    Return *the length of the shortest subarray to remove*.

    A **subarray** is a contiguous subsequence of the array.

    """

    def find_length_of_shortest_subarray(self, arr: list[int]) -> int:
        n = len(arr)

        # Find the longest prefix which is sorted
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        # If the entire array is sorted, return 0
        if left == n - 1:
            return 0

        # Find the longest suffix which is sorted
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # If we can merge prefix and suffix by removing elements between them, find the min
        # Either remove from left or right
        result = min(n - left - 1, right)

        # Try to merge prefix and suffix by removing less
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1

        return result

    findLengthOfShortestSubarray = find_length_of_shortest_subarray
