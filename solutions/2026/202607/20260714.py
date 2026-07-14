# https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/


class Solution:
    """3336. Find the Number of Subsequences With Equal GCD

    You are given an integer array `nums`.

    Your task is to find the number of pairs of **non-empty** subsequences `(seq1,
    seq2)` of `nums` that satisfy the following conditions:

    * The subsequences `seq1` and `seq2` are **disjoint**, meaning **no index** of
    `nums` is common between them.

    * The GCD of the elements of `seq1` is equal to the GCD of the elements of `seq2`.

    Return the total number of such pairs.

    Since the answer may be very large, return it **modulo** `109 + 7`.

    Constraints:

    * `1 <= nums.length <= 200`

    * `1 <= nums[i] <= 200`"""

    def subsequence_pair_count(self, nums: list[int]) -> int: ...

    subsequencePairCount = subsequence_pair_count
