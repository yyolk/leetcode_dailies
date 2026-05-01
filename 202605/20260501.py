# https://leetcode.com/problems/rotate-function/

class Solution:
    """396. Rotate Function

    You are given an integer array nums of length n. Assume arrk to be an array
    obtained by rotating nums by k positions clock-wise. We define the rotation
    function F on nums as follow: F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n -
    1) * arrk[n - 1]. Return the maximum value of F(0), F(1), ..., F(n-1). The
    test cases are generated so that the answer fits in a 32-bit integer.
    """
    def max_rotate_function(self, nums: list[int]) -> int:
        n = len(nums)
        # precompute sum S for O(1) updates per rotation
        total = sum(nums)
        # compute F(0) = sum(i * nums[i] for i in range(n))
        f = sum(i * nums[i] for i in range(n))
        max_f = f
        for k in range(1, n):
            # F(k) = F(k-1) + total - n * nums[n-k]
            # nums[n-k] is element moving from index n-1 to 0
            f += total - n * nums[n - k]
            max_f = max(max_f, f)
        return max_f

    maxRotateFunction = max_rotate_function