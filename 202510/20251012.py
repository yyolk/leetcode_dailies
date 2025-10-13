# https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/
# Define the modulus for large numbers
MOD = 10**9 + 7


class Solution:
    """3539. Find Sum of Array Product of Magical Sequences

    You are given two integers, `m` and `k`, and an integer array `nums`.

    A sequence of integers `seq` is called **magical** if:

    * `seq` has a size of `m`.

    * `0 <= seq[i] < nums.length`

    * The **binary representation** of `2seq[0] + 2seq[1] + ... + 2seq[m - 1]` has `k`
    **set bits**.

    The **array product** of this sequence is defined as `prod(seq) = (nums[seq[0]] *
    nums[seq[1]] * ... * nums[seq[m - 1]])`.

    Return the **sum** of the **array products** for all valid **magical** sequences.

    Since the answer may be large, return it **modulo** `109 + 7`.

    A **set bit** refers to a bit in the binary representation of a number that has a
    value of 1."""

    def magical_sum(self, m: int, k: int, nums: list[int]) -> int:
        # Get the length of nums
        n = len(nums)
        # Precompute binomial coefficients C(i, j) for i, j <= m
        binom = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            binom[i][0] = 1
            for j in range(1, i + 1):
                # Compute binomial using previous values
                binom[i][j] = (binom[i - 1][j - 1] + binom[i - 1][j]) % MOD
        # Precompute powers nums[i]^f % MOD for each i and f <= m
        pows = [[0] * (m + 1) for _ in range(n)]
        for i in range(n):
            pows[i][0] = 1
            for f in range(1, m + 1):
                # Compute next power by multiplying previous
                pows[i][f] = (pows[i][f - 1] * nums[i]) % MOD
        # Use lru_cache for memoization
        from functools import lru_cache

        @lru_cache(None)
        def dfs(pos: int, rem: int, carry: int, ones: int) -> int:
            # Base case: processed all positions
            if pos == n:
                if rem > 0:
                    return 0
                # Calculate extra set bits from remaining carry
                extra = bin(carry).count("1")
                # Check if total set bits match k
                if ones + extra == k:
                    return 1
                return 0
            res = 0
            for f in range(rem + 1):
                # Compute contribution: C(rem, f) * nums[pos]^f % MOD
                val = (binom[rem][f] * pows[pos][f]) % MOD
                # Compute total at current bit: choices + incoming carry
                total = f + carry
                # Determine if bit is set
                bit = total % 2
                # Compute outgoing carry
                cout = total // 2
                # Update count of set bits
                new_ones = ones + bit
                # Skip if exceeding k set bits
                if new_ones > k:
                    continue
                # Recurse to next position
                sub = dfs(pos + 1, rem - f, cout, new_ones)
                # Accumulate the result
                res = (res + val * sub) % MOD
            return res

        # Start DFS from position 0, remaining m, carry 0, ones 0
        return dfs(0, m, 0, 0)

    magicalSum = magical_sum
