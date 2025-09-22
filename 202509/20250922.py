# https://leetcode.com/problems/count-elements-with-maximum-frequency/


class Solution:
    """3005. Count Elements With Maximum Frequency

    You are given an array `nums` consisting of **positive** integers.

    Return *the **total frequencies** of elements in*`nums` *such that those elements
    all have the **maximum** frequency*.

    The **frequency** of an element is the number of occurrences of that element in the
    array."""

    def max_frequency_elements(self, nums: list[int]) -> int:
        # Initialize frequency dictionary to count occurrences of each element
        freq = {}
        for num in nums:
            # Increment count for the current number, default to 0 if not present
            freq[num] = freq.get(num, 0) + 1
        
        # Handle empty list case, though problem assumes positive integers array
        if not freq:
            return 0
        
        # Find the maximum frequency value among all elements
        max_freq = max(freq.values())
        
        # Initialize total to sum frequencies equal to max_freq
        total = 0
        for f in freq.values():
            # Add frequency if it matches the maximum
            if f == max_freq:
                total += f
        
        # Return the sum, which is count of max freq elements times max_freq
        return total

    maxFrequencyElements = max_frequency_elements
