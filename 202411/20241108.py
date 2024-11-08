# https://leetcode.com/problems/maximum-xor-for-each-query/


class Solution:
    """1829. Maximum XOR for Each Query

    You are given a **sorted** array `nums` of `n` non\\-negative integers and an integer
    `maximum_bit`. You want to perform the following query `n` **times**:

    1. Find a non\\-negative integer `k < 2maximum_bit` such that `nums[0] XOR nums[1]
    XOR ... XOR nums[nums.length-1] XOR k` is **maximized**. `k` is the answer to the
    `ith` query.

    2. Remove the **last** element from the current array `nums`.

    Return *an array* `answer`*, where* `answer[i]` *is the answer to the* `ith`
    *query*.

    """

    def get_maximum_xor(self, nums: list[int], maximum_bit: int) -> list[int]:
        # Create a bitmask with all bits set to 1 from 0 to maximum_bit-1
        bitmask = (1 << maximum_bit) - 1

        # Get the length of nums
        total_numbers = len(nums)

        # Initialize result array to store the maximum XOR for each query
        query_results = [0] * total_numbers

        # Start with the cumulative XOR of all numbers in nums
        cumulative_xor = 0

        # Iterate through each number in nums
        for index in range(total_numbers):
            # Update the cumulative XOR with the current number
            cumulative_xor ^= nums[index]

            # The result for query at index (remember we fill from the end towards the start)
            # is the bitwise complement of the cumulative XOR, but only within the bitmask
            # This effectively finds the largest number k that maximizes XOR with cumulative_xor
            query_results[total_numbers - index - 1] = ~cumulative_xor & bitmask

        # Return the list of results where each element is the answer for each query
        return query_results

    getMaximumXor = get_maximum_xor
