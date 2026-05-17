# https://leetcode.com/problems/k-inverse-pairs-array/
MOD = 10**9 + 7


class Solution:
    """629. K Inverse Pairs Array

    For an integer array `nums`, an **inverse pair** is a pair of integers `[i, j]`
    where `0 <= i < j < nums.length` and `nums[i] > nums[j]`.

    Given two integers n and k, return the number of different arrays consist of numbers
    from `1` to `n` such that there are exactly `k` **inverse pairs**. Since the answer
    can be huge, return it **modulo** `109 + 7`.

    """

    def k_inverse_pairs(self, n: int, k: int) -> int:
        # Initialize a dynamic programming array with base case
        dp = [1] + [0] * k

        # Iterate through the possible array lengths
        for i in range(n):
            tmp, sm = [], 0
            # Iterate through the possible number of inverse pairs
            for j in range(k + 1):
                # Calculate the total number of inverse pairs
                sm += dp[j]
                if j - i >= 1:
                    # Subtract the contribution from the previous array length
                    sm -= dp[j - i - 1]
                sm %= MOD
                tmp.append(sm)
            # Update the dynamic programming array for the next iteration
            dp = tmp

        return dp[k]

    kInversePairs = k_inverse_pairs
