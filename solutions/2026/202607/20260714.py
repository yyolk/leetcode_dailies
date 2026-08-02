# https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

from math import gcd


class Solution:
    """3336. Find the Number of Subsequences With Equal GCD

    You are given an integer array `nums`.
    Your task is to find the number of pairs of **non-empty** subsequences
    `(seq1, seq2)` of `nums` that satisfy the following conditions:
    * The subsequences `seq1` and `seq2` are **disjoint**, meaning **no
      index** of `nums` is common between them.
    * The GCD of the elements of `seq1` is equal to the GCD of the elements
      of `seq2`.
    Return the total number of such pairs.
    Since the answer may be very large, return it **modulo** `10^9 + 7`.
    Constraints:
    * `1 <= nums.length <= 200`
    * `1 <= nums[i] <= 200`
    """

    def subsequence_pair_count(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        max_num = max(nums)
        # dp[x][y]: ways for two disjoint subsequences with gcd x and y so far
        # (0 means empty subsequence)
        dp = [[0] * (max_num + 1) for _ in range(max_num + 1)]
        dp[0][0] = 1  # start with two empty sequences

        for num in nums:
            # new_dp for after deciding on current num
            new_dp = [[0] * (max_num + 1) for _ in range(max_num + 1)]
            for x in range(max_num + 1):
                for y in range(max_num + 1):
                    if dp[x][y] == 0:
                        continue
                    ways = dp[x][y]
                    # skip current num (not in either subsequence)
                    new_dp[x][y] = (new_dp[x][y] + ways) % mod
                    # add num to first subsequence
                    nx = gcd(x, num)
                    new_dp[nx][y] = (new_dp[nx][y] + ways) % mod
                    # add num to second subsequence
                    ny = gcd(y, num)
                    new_dp[x][ny] = (new_dp[x][ny] + ways) % mod
            dp = new_dp

        # sum ways where both non-empty and equal gcd
        ans = 0
        for g in range(1, max_num + 1):
            ans = (ans + dp[g][g]) % mod
        return ans

    subsequencePairCount = subsequence_pair_count
