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

    def unique_xor_triplets(self, nums: list[int]) -> int:
        n = len(nums)
        # i <= j <= k allows repeated indices, so for n <= 2:
        # n = 1 -> {1}, n = 2 -> {1, 2}.
        if n <= 2:
            return n
        max_value = n  # nums is a permutation of [1..n]
        # For any n >= 3 (nums is a permutation of [1..n]), reachable XOR values
        # cover all numbers in [0, 2^bit_length(n) - 1].
        return 1 << max_value.bit_length()

    uniqueXorTriplets = unique_xor_triplets
