# https://leetcode.com/problems/height-checker/


class Solution:
    """1051. Height Checker

    A school is trying to take an annual photo of all the students. The students are
    asked to stand in a single file line in **non-decreasing order** by height. Let this
    ordering be represented by the integer array `expected` where `expected[i]` is the
    expected height of the `ith` student in line.

    You are given an integer array `heights` representing the **current order** that the
    students are standing in. Each `heights[i]` is the height of the `ith` student in
    line (**0-indexed**).

    Return *the **number of indices** where* `heights[i] != expected[i]`.

    """

    def height_checker(self, heights: list[int]) -> int:
        # Sort the heights to get the expected order
        sorted_heights = sorted(heights)
        # Count the mismatches between the current order and the expected order
        return sum(
            1 for expected, actual in zip(sorted_heights, heights) if expected != actual
        )

    heightChecker = height_checker
