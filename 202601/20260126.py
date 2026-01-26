# https://leetcode.com/problems/minimum-absolute-difference


class Solution:
    """1200. Minimum Absolute Difference

    Given an array of distinct integers arr, find all pairs of elements with the
    minimum absolute difference of any two elements.

    Return a list of pairs in ascending order(with respect to pairs), each pair
    [a, b] follows

    a, b are from arr
    a < b
    b - a equals to the minimum absolute difference of any two elements in arr
    """
    def minimum_abs_difference(self, arr: list[int]) -> list[list[int]]:
        if len(arr) < 2:
            return []

        # Sort once → O(n log n)
        arr.sort()

        # Find minimum difference in one pass
        min_diff = float("inf")
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < min_diff:
                min_diff = diff

        # Collect all pairs with exactly that difference
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                result.append([arr[i-1], arr[i]])

        return result

    minimumAbsDifference = minimum_abs_difference