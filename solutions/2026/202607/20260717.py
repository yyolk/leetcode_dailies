# https://leetcode.com/problems/sorted-gcd-pair-queries/

import bisect


class Solution:
    """3312. Sorted GCD Pair Queries

    You are given an integer array nums of length n and an integer array
    queries. Let gcdPairs denote an array obtained by calculating the GCD of
    all possible pairs (nums[i], nums[j]), where 0 <= i < j < n, and then
    sorting these values in ascending order. For each query queries[i], you
    need to find the element at index queries[i] in gcdPairs. Return an
    integer array answer, where answer[i] is the value at
    gcdPairs[queries[i]] for each query. The term gcd(a, b) denotes the
    greatest common divisor of a and b.
    Constraints:
    * 2 <= n == nums.length <= 10^5
    * 1 <= nums[i] <= 5 * 10^4
    * 1 <= queries.length <= 10^5
    * 0 <= queries[i] < n * (n - 1) / 2"""

    def gcd_values(self, nums: list[int], queries: list[int]) -> list[int]:
        # max value bounds all possible GCDs
        max_num = max(nums)
        # frequency of each number in nums
        freq = [0] * (max_num + 1)
        for x in nums:
            freq[x] += 1
        # mult[d]: how many nums are divisible by d
        mult = [0] * (max_num + 1)
        for d in range(1, max_num + 1):
            for m in range(d, max_num + 1, d):
                mult[d] += freq[m]
        # f[d]: number of pairs where d divides both (i.e. d | gcd)
        f = [0] * (max_num + 1)
        for d in range(1, max_num + 1):
            c = mult[d]
            f[d] = c * (c - 1) // 2
        # mobius function mu via linear sieve
        mu = [0] * (max_num + 1)
        is_composite = [False] * (max_num + 1)
        primes = []
        mu[1] = 1
        for i in range(2, max_num + 1):
            if not is_composite[i]:
                primes.append(i)
                mu[i] = -1
            for p in primes:
                if i * p > max_num:
                    break
                is_composite[i * p] = True
                if i % p == 0:
                    mu[i * p] = 0
                    break
                else:
                    mu[i * p] = -mu[i]
        # exact[d]: pairs with gcd(nums[i], nums[j]) == d exactly
        exact = [0] * (max_num + 1)
        for d in range(1, max_num + 1):
            for k in range(1, max_num // d + 1):
                exact[d] += mu[k] * f[d * k]
        # cum[d]: number of pairs with gcd <= d (prefix sum)
        cum = [0] * (max_num + 1)
        for d in range(1, max_num + 1):
            cum[d] = cum[d - 1] + exact[d]
        # for each 0-based query index q find min d where cum[d] > q
        return [bisect.bisect_right(cum, q) for q in queries]

    gcdValues = gcd_values
