# https://leetcode.com/problems/number-of-unique-xor-triplets-i/


class Solution:
    """3513. Number of Unique XOR Triplets I

    You are given an integer array `nums` of length `n`, where `nums` is a
    **permutation** of the numbers in the range `[1, n]`.

    A **XOR triplet** is defined as the XOR of three elements `nums[i] XOR nums[j] XOR
    nums[k]` where `i <= j <= k`.

    Return the number of **unique** XOR triplet values from all possible triplets `(i,
    j, k)`.

    Constraints:

    * `1 <= n == nums.length <= 105`

    * `1 <= nums[i] <= n`

    * `nums` is a permutation of integers from `1` to `n`."""

    def unique_xor_triplets(self, nums: list[int]) -> int: ...

    uniqueXorTriplets = unique_xor_triplets
