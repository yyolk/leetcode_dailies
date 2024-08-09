# https://leetcode.com/problems/magic-squares-in-grid/


class Solution:
    """840. Magic Squares In Grid

    A `3 x 3` **magic square** is a `3 x 3` grid filled with distinct numbers **from** 1
    **to** 9 such that each row, column, and both diagonals all have the same sum.

    Given a `row x col` `grid` of integers, how many `3 x 3` contiguous magic square
    subgrids are there?

    Note: while a magic square can only contain numbers from 1 to 9, `grid` may contain
    numbers up to 15\\.

    """

    def num_magic_squares_inside(self, grid: list[list[int]]) -> int: ...

    numMagicSquaresInside = num_magic_squares_inside
