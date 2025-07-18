# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/


class Solution:
    """3202. Find the Maximum Length of Valid Subsequence II

    You are given an integer array `nums` and a **positive** integer `k`.

    A subsequence `sub` of `nums` with length `x` is called **valid** if it satisfies:

    * `(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x -
    1]) % k.`

    Return the length of the **longest** **valid** subsequence of `nums`."""

    def maximum_length(self, nums: list[int], k: int) -> int:
        if not nums:
            return 0
        ans = 1
        for r in range(k):
            max_len = [0] * k
            for num in nums:
                res = num % k
                prev = (r - res) % k
                newl = 1
                if max_len[prev] > 0:
                    newl = max_len[prev] + 1
                max_len[res] = max(max_len[res], newl)
            ans = max(ans, max(max_len))
        return ans

    maximumLength = maximum_length
