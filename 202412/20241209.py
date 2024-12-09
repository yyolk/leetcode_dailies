# https://leetcode.com/problems/special-array-ii/


class Solution:
    """3152. Special Array II

    An array is considered **special** if every pair of its adjacent elements contains
    two numbers with different parity.

    You are given an array of integer `nums` and a 2D integer matrix `queries`, where
    for `queries[i] = [fromi, toi]` your task is to check that subarray
    `nums[fromi..toi]` is **special** or not.

    Return an array of booleans `answer` such that `answer[i]` is `true` if
    `nums[fromi..toi]` is special."""

    def is_array_special(
        self, nums: list[int], queries: list[list[int]]
    ) -> list[bool]:
        n = len(nums)
        # Prefix array to count special pairs
        prefix = [0] * n

        # Build the prefix array
        for i in range(1, n):
            prefix[i] = prefix[i - 1]
            if (nums[i - 1] % 2 == 0 and nums[i] % 2 == 0) or (nums[i - 1] % 2 != 0 and nums[i] % 2 != 0):
                prefix[i] += 1

        result = []

        # Process each query
        for left, right in queries:
            special_count = prefix[right] - (prefix[left] if left > 0 else 0)
            result.append(special_count == 0)

        return result

    isArraySpecial = is_array_special
