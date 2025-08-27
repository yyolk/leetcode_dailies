# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/


class Solution:
    """3459. Length of Longest V-Shaped Diagonal Segment

    You are given a 2D integer matrix `grid` of size `n x m`, where each element is
    either `0`, `1`, or `2`.

    A **V-shaped diagonal segment** is defined as:

    * The segment starts with `1`.

    * The subsequent elements follow this infinite sequence: `2, 0, 2, 0, ...`.

    * The segment:

      + Starts **along** a diagonal direction (top-left to bottom-right, bottom-right to
    top-left, top-right to bottom-left, or bottom-left to top-right).

      + Continues the **sequence** in the same diagonal direction.

      + Makes **at most one clockwise 90-degree** **turn** to another diagonal direction
    while **maintaining** the sequence.

    ![](https://assets.leetcode.com/uploads/2025/01/11/length_of_longest3.jpg)

    Return the **length** of the **longest** **V-shaped diagonal segment**. If no valid
    segment *exists*, return 0."""

    def len_of_v_diagonal(self, grid: list[list[int]]) -> int: ...

    lenOfVDiagonal = len_of_v_diagonal
