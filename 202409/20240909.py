# https://leetcode.com/problems/spiral-matrix-iv/


class Solution:
    """2326. Spiral Matrix IV

    You are given two integers `m` and `n`, which represent the dimensions of a matrix.

    You are also given the `head` of a linked list of integers.

    Generate an `m x n` matrix that contains the integers in the linked list presented
    in **spiral** order **(clockwise)**, starting from the **top\\-left** of the matrix.
    If there are remaining empty spaces, fill them with `-1`.

    Return *the generated matrix*.

    """

    def spiral_matrix(
        self, m: int, n: int, head: Optional[ListNode]
    ) -> list[list[int]]: ...

    spiralMatrix = spiral_matrix
