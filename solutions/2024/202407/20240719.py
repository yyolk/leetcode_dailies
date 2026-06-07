# https://leetcode.com/problems/lucky-numbers-in-a-matrix/


class Solution:
    """1380. Lucky Numbers in a Matrix

    Given an `m x n` matrix of **distinct** numbers, return *all **lucky numbers** in
    the matrix in **any** order*.

    A **lucky number** is an element of the matrix such that it is the minimum element
    in its row and maximum in its column.

    """

    def lucky_numbers(self, matrix: list[list[int]]) -> list[int]:
        # Step 1: Find the minimum element in each row
        min_in_row = {min(row) for row in matrix}

        # Step 2: Find the maximum element in each column
        max_in_col = {max(col) for col in zip(*matrix)}

        # Step 3: The intersection of the two sets will be our lucky numbers
        lucky_nums = list(min_in_row & max_in_col)

        return lucky_nums

    luckyNumbers = lucky_numbers
