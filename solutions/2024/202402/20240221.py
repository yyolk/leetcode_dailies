# https://leetcode.com/problems/bitwise-and-of-numbers-range/


class Solution:
    """201. Bitwise AND of Numbers Range

    Given two integers `left` and `right` that represent the range `[left, right]`,
    return *the bitwise AND of all numbers in this range, inclusive*.

    """

    def range_bitwise_and(self, left: int, right: int) -> int:
        shift = 0
        # Find the common prefix of the binary representations of left and right
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        # Left shift back to obtain the final result
        return left << shift

    rangeBitwiseAnd = range_bitwise_and
