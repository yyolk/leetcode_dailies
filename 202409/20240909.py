# https://leetcode.com/problems/spiral-matrix-iv/


class Solution:
    """2326. Spiral Matrix IV

    You are given two integers `m` and `n`, which represent the dimensions of a matrix.

    You are also given the `head` of a linked list of integers.

    Generate an `m x n` matrix that contains the integers in the linked list presented
    in **spiral** order **(clockwise)**, starting from the **top\\-left** of the matrix.
    If there are remaining empty spaces, fill them with `-1`.

    Return *the generated matrix*.

    Definition for singly-linked list::

        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
    """

    def spiral_matrix(
        self, m: int, n: int, head: Optional[ListNode]
    ) -> list[list[int]]:
        # Initialize the matrix with -1
        matrix = [[-1 for _ in range(n)] for _ in range(m)]

        # If the list is empty or matrix dimensions are invalid, return the matrix
        if not head or m == 0 or n == 0:
            return matrix

        # Define directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Starting position and direction
        row, col, d = 0, 0, 0

        # Fill the matrix
        while head:
            matrix[row][col] = head.val

            # Move to the next position
            next_row, next_col = row + directions[d][0], col + directions[d][1]

            # Check if we can move in the current direction
            if (
                0 <= next_row < m
                and 0 <= next_col < n
                and matrix[next_row][next_col] == -1
            ):
                row, col = next_row, next_col
            else:
                # Change direction
                d = (d + 1) % 4
                row, col = row + directions[d][0], col + directions[d][1]

            head = head.next

        return matrix

    spiralMatrix = spiral_matrix
