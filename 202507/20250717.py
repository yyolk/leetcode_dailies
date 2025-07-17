# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/


class Solution:
    """3202. Find the Maximum Length of Valid Subsequence II

    You are given an integer array `nums` and a **positive** integer `k`.

    A subsequence `sub` of `nums` with length `x` is called **valid** if it satisfies:

    * `(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x -
    1]) % k.`

    Return the length of the **longest** **valid** subsequence of `nums`."""

    def maximum_length(self, nums: list[int], k: int) -> int: ...

    maximumLength = maximum_length
