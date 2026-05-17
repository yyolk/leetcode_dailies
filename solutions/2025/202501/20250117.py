# https://leetcode.com/problems/neighboring-bitwise-xor/


class Solution:
    """2683. Neighboring Bitwise XOR

    A **0-indexed** array `derived` with length `n` is derived by computing the
    **bitwise XOR** (⊕) of adjacent values in a **binary array** `original` of length
    `n`.

    Specifically, for each index `i` in the range `[0, n - 1]`:

    * If `i = n - 1`, then `derived[i] = original[i] ⊕ original[0]`.

    * Otherwise, `derived[i] = original[i] ⊕ original[i + 1]`.

    Given an array `derived`, your task is to determine whether there exists a **valid
    binary array** `original` that could have formed `derived`.

    Return ***true** if such an array exists or **false** otherwise.*

    * A binary array is an array containing only **0's** and **1's**"""

    def does_valid_array_exist(self, derived: list[int]) -> bool:
        # The key idea here is that the XOR of all elements in 'derived'
        # should be 0 for a valid 'original' array to exist because:
        # If we XOR all equations:
        # derived[0] ^ derived[1] ^ ... ^ derived[n-1] =
        # (original[0] ^ original[1]) ^ (original[1] ^ original[2]) ^ ... ^ (original[n-1] ^ original[0])
        # This simplifies to original[0] ^ original[0] ^ ... ^ original[n-1] ^ original[n-1] which should be 0

        xor_result = 0
        for num in derived:
            xor_result ^= num

        # If the XOR of all numbers in derived is 0, then a valid original array exists
        return xor_result == 0

    doesValidArrayExist = does_valid_array_exist
