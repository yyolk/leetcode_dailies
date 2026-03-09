# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i

class Solution:
    """3129. Find All Possible Stable Binary Arrays I
    
    You are given three positive integers zero, one, and limit. A binary array
    arr is considered stable if it satisfies all three conditions: It contains
    exactly zero number of 0s. It contains exactly one number of 1s. Every
    subarray of size greater than limit must contain both 0 and 1. In other
    words, no subarray of length limit + 1 or more can consist entirely of the
    same digit (i.e., no more than limit consecutive 0s or 1s are allowed).
    Return the total number of stable binary arrays modulo 10^9 + 7.
    """
    def number_of_stable_arrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1_000_000_007
        # dp[i][j][0/1]: ways using exactly i zeros and j ones ending with 0/1
        # (all prefixes satisfy no run > limit)
        dp = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # base: all-zeros (if run <= limit)
        for i in range(min(zero, limit) + 1):
            dp[i][0][0] = 1
        # base: all-ones (if run <= limit)
        for j in range(min(one, limit) + 1):
            dp[0][j][1] = 1
        
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # append 0: total from i-1 zeros + subtract those ending with
                # exactly limit zeros (would make limit+1)
                sub = dp[i - limit - 1][j][1] if i - limit >= 1 else 0
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1] - sub + MOD) % MOD
                
                # append 1: total from j-1 ones + subtract those ending with
                # exactly limit ones
                sub = dp[i][j - limit - 1][0] if j - limit >= 1 else 0
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1] - sub + MOD) % MOD
        
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD

    numberOfStableArrays = number_of_stable_arrays