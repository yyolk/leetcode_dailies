# https://leetcode.com/problems/sum-of-subarray-minimums/
MOD = 10**9 + 7


class Solution:
    """907. Sum of Subarray Minimums

    Given an array of integers arr, find the sum of `min(b)`, where `b` ranges over
    every (contiguous) subarray of `arr`. Since the answer may be large, return the
    answer **modulo** `109 + 7`.
    """

    def sum_subarray_mins(self, arr: list[int]) -> int:
        n = len(arr)
        left_boundaries = [0] * n
        right_boundaries = [0] * n
        stack = []

        # Find left boundaries
        for i in range(n):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            left_boundaries[i] = stack[-1] if stack else -1
            stack.append(i)

        # Clear the stack for right boundaries
        stack = []

        # Find right boundaries
        for i in range(n - 1, -1, -1):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            right_boundaries[i] = stack[-1] if stack else n
            stack.append(i)

        # Calculate the sum of min(b)
        result = 0
        for i in range(n):
            result = (result + arr[i] * (i - left_boundaries[i]) * (right_boundaries[i] - i)) % MOD

        return result
    sumSubarrayMins = sum_subarray_mins
