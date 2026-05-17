# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/


class Solution:
    """1769. Minimum Number of Operations to Move All Balls to Each Box

    You have `n` boxes. You are given a binary string `boxes` of length `n`, where
    `boxes[i]` is `"0"` if the `ith` box is **empty**, and `"1"` if it contains **one**
    ball.

    In one operation, you can move **one** ball from a box to an adjacent box. Box `i`
    is adjacent to box `j` if `abs(i - j) == 1`. Note that after doing so, there may be
    more than one ball in some boxes.

    Return an array `answer` of size `n`, where `answer[i]` is the **minimum** number of
    operations needed to move all the balls to the `ith` box.

    Each `answer[i]` is calculated considering the **initial** state of the boxes."""

    def min_operations(self, boxes: str) -> list[int]:
        n = len(boxes)
        answer = [0] * n

        # First pass: Count balls to the left for each position
        count_left = 0
        cost_left = 0
        for i in range(n):
            answer[i] += cost_left
            if boxes[i] == "1":
                count_left += 1
            cost_left += count_left

        # Second pass: Count balls to the right for each position
        count_right = 0
        cost_right = 0
        for i in range(n - 1, -1, -1):
            answer[i] += cost_right
            if boxes[i] == "1":
                count_right += 1
            cost_right += count_right

        return answer

    minOperations = min_operations
