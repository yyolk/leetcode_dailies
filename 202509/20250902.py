# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/


class Solution:
    """3025. Find the Number of Ways to Place People I

    You are given a 2D array `points` of size `n x 2` representing integer coordinates
    of some points on a 2D plane, where `points[i] = [xi, yi]`.

    Count the number of pairs of points `(A, B)`, where

    * `A` is on the **upper left** side of `B`, and

    * there are no other points in the rectangle (or line) they make (**including the
    border**).

    Return the count."""

    def number_of_pairs(self, points: list[list[int]]) -> int: ...

    numberOfPairs = number_of_pairs
