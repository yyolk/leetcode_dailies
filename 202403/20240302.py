# https://leetcode.com/problems/squares-of-a-sorted-array/


class Solution:
    """977. Squares of a Sorted Array

    Given an integer array `nums` sorted in **non-decreasing** order, return *an array
    of **the squares of each number** sorted in non-decreasing order*.

    """

    def sorted_squares(self, nums: list[int]) -> list[int]:
        # Square each element in the array
        squares = [num ** 2 for num in nums]

        # Sort the squared values in non-decreasing order
        sorted_squares = sorted(squares)

        return sorted_squares

    sortedSquares = sorted_squares
