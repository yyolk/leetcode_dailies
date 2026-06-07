# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
from collections import defaultdict


class Solution:
    """2275. Largest Combination With Bitwise AND Greater Than Zero

    The **bitwise AND** of an array `nums` is the bitwise AND of all integers in `nums`.

    * For example, for `nums = [1, 5, 3]`, the bitwise AND is equal to `1 & 5 & 3 = 1`.

    * Also, for `nums = [7]`, the bitwise AND is `7`.

    You are given an array of positive integers `candidates`. Evaluate the **bitwise
    AND** of every **combination** of numbers of `candidates`. Each number in
    `candidates` may only be used **once** in each combination.

    Return *the size of the **largest** combination of* `candidates` *with a bitwise AND
    **greater** than* `0`.

    """

    def largest_combination(self, candidates: list[int]) -> int:
        # Use a defaultdict to count how many numbers have each bit set
        bit_counts = defaultdict(int)

        # Count the occurrences of each bit set across all numbers
        for num in candidates:
            # Assuming 32-bit integers
            for bit in range(32):
                if num & (1 << bit):
                    bit_counts[bit] += 1

        # The maximum count is the answer since it represents the largest subset
        # with all numbers having that bit set, thus AND > 0 for this subset
        return max(bit_counts.values()) if bit_counts else 0

    largestCombination = largest_combination
