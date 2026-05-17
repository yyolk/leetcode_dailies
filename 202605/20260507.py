# https://leetcode.com/problems/jump-game-ix/


class Solution:
    """3660. Jump Game IX

    You are given an integer array nums. From any index i, you can jump to
    another index j under the following rules: Jump to index j where j > i
    is allowed only if nums[j] < nums[i]. Jump to index j where j < i is
    allowed only if nums[j] > nums[i]. For each index i, find the maximum
    value in nums that can be reached by following any sequence of valid
    jumps starting at i. Return an array ans where ans[i] is the maximum
    value reachable starting from index i.
    """

    def max_value(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if not n:
            return []
        # pre_max[i] holds the maximum value in nums[0..i] inclusive
        pre_max = [0] * n
        pre_max[0] = nums[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])
        ans = [0] * n
        # suf_min will track the minimum value from the current i + 1 to n - 1
        suf_min = float("inf")
        for i in range(n - 1, -1, -1):
            # If the max value up to i exceeds the min value on its right,
            # a position holding pre_max[i] (reachable from i) can jump
            # right to the right-side minimum; from there any higher value
            # reachable from i + 1 can be reached by left jumps (higher > min)
            if i + 1 < n and pre_max[i] > suf_min:
                ans[i] = ans[i + 1]
            else:
                ans[i] = pre_max[i]
            # Include nums[i] into suf_min for positions further left
            suf_min = min(suf_min, nums[i])
        return ans

    maxValue = max_value
