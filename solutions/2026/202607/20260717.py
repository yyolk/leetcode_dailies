# https://leetcode.com/problems/sorted-gcd-pair-queries/


class Solution:
    """3312. Sorted GCD Pair Queries

    You are given an integer array `nums` of length `n` and an integer array `queries`.

    Let `gcdPairs` denote an array obtained by calculating the GCD of all possible pairs
    `(nums[i], nums[j])`, where `0 <= i < j < n`, and then sorting these values in
    **ascending** order.

    For each query `queries[i]`, you need to find the element at index `queries[i]` in
    `gcdPairs`.

    Return an integer array `answer`, where `answer[i]` is the value at
    `gcdPairs[queries[i]]` for each query.

    The term `gcd(a, b)` denotes the **greatest common divisor** of `a` and `b`.

    Constraints:

    * `2 <= n == nums.length <= 105`

    * `1 <= nums[i] <= 5 * 104`

    * `1 <= queries.length <= 105`

    * `0 <= queries[i] < n * (n - 1) / 2`"""

    def gcd_values(self, nums: list[int], queries: list[int]) -> list[int]: ...

    gcdValues = gcd_values
