# https://leetcode.com/problems/count-the-number-of-ideal-arrays/
from collections import Counter
from math import comb

MOD = 1_000_000_007


class Solution:
    """2338. Count the Number of Ideal Arrays

    You are given two integers `n` and `max_value`, which are used to describe an
    **ideal** array.

    A **0-indexed** integer array `arr` of length `n` is considered **ideal** if the
    following conditions hold:

    * Every `arr[i]` is a value from `1` to `max_value`, for `0 <= i < n`.

    * Every `arr[i]` is divisible by `arr[i - 1]`, for `0 < i < n`.

    Return *the number of **distinct** ideal arrays of length* `n`. Since the answer may
    be very large, return it modulo `10^9 + 7`."""

    def ideal_arrays(self, n: int, max_value: int) -> int:
        # Initialize total_ways with the number of possible arrays of length 1
        # Each number from 1 to max_value can be the first element
        total_ways = max_value

        # Initialize frequency_map where each number from 1 to max_value has frequency 1
        # This represents the count of arrays of length 1 ending with each number
        frequency_map = {num: 1 for num in range(1, max_value + 1)}

        # Build arrays from length 1 to n-1 (since length 1 is already counted)
        for array_size in range(1, n):
            # Create a new Counter to store frequencies of numbers for the next array size
            new_frequency = Counter()

            # For each current ending number (base_value) in frequency_map
            for base_value in frequency_map:
                # Try multipliers starting from 2 to generate next possible values
                # Only go up to max_value // base_value to stay within max_value
                for multiplier in range(2, max_value // base_value + 1):
                    # Calculate the next value in the sequence
                    next_value = multiplier * base_value

                    # Calculate number of ways to place this next_value in arrays of current size
                    # comb(n-1, array_size) gives ways to choose positions for remaining elements
                    combinations = comb(n - 1, array_size)

                    # Add to total_ways: combinations * frequency of base_value
                    total_ways += combinations * frequency_map[base_value]

                    # Update frequency of next_value for the next iteration
                    new_frequency[next_value] += frequency_map[base_value]

            # Update frequency_map for the next array size
            frequency_map = new_frequency

            # Apply modulo to prevent overflow
            total_ways %= MOD

        # Return the total number of distinct ideal arrays
        return total_ways

    idealArrays = ideal_arrays
