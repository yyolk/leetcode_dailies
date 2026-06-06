# https://leetcode.com/problems/left-and-right-sum-differences/


class Solution:
    """2574. Left and Right Sum Differences

    You are given a **0-indexed** integer array `nums` of size `n`.

    Define two arrays `leftSum` and `rightSum` where:

    * `leftSum[i]` is the sum of elements to the left of the index `i` in the array
    `nums`. If there is no such element, `leftSum[i] = 0`.

    * `rightSum[i]` is the sum of elements to the right of the index `i` in the array
    `nums`. If there is no such element, `rightSum[i] = 0`.

    Return an integer array `answer` of size `n` where `answer[i] = |leftSum[i] -
    rightSum[i]|`."""

    def left_right_difference(self, nums: list[int]) -> list[int]: ...

    leftRightDifference = left_right_difference
