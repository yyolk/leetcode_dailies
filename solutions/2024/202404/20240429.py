# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/


class Solution:
    """2997. Minimum Number of Operations to Make Array XOR Equal to K

    You are given a **0-indexed** integer array `nums` and a positive integer `k`.

    You can apply the following operation on the array **any** number of times:

    * Choose **any** element of the array and **flip** a bit in its **binary**
    representation. Flipping a bit means changing a `0` to `1` or vice versa.

    Return *the **minimum** number of operations required to make the bitwise* `XOR` *of
    **all** elements of the final array equal to* `k`.

    **Note** that you can flip leading zero bits in the binary representation of
    elements. For example, for the number `(101)2` you can flip the fourth bit and
    obtain `(1101)2`.

    """

    def min_operations(self, nums: list[int], k: int) -> int:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        # XOR of all elements in nums is xor_sum
        # To make the XOR equal to k, we need to find the minimum number of bit flips
        # required in xor_sum to obtain k
        # This is equivalent to finding the XOR of xor_sum and k
        target_xor = xor_sum ^ k

        # Count the number of set bits in target_xor
        count_set_bits = bin(target_xor).count("1")

        return count_set_bits

    minOperations = min_operations
